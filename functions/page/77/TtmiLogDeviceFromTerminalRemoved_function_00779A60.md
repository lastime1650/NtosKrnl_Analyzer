# TtmiLogDeviceFromTerminalRemoved

- RVA: `0x00779A60`–`0x00779B8C` (길이 `300` bytes)
- VA: `0x0000000140779A60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD9C`
- 디코드: `71`개 명령, `300/300` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00779AB1` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00779ACE` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00779B5D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00779B69` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiEvacuateDevices](TtmiEvacuateDevices_function_00775BA4.md) at `0x00775BD7`

### Static image references
- `0x00779A7F` → RVA `0x00E0A740` (`.data`; read)
- `0x00779A8D` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00779B34` → RVA `0x00052616` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00779AB1` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00779ACE` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00779B5D` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00779B69` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779A60  48 8B C4                        mov rax, rsp
00779A63  48 89 58 08                     mov qword ptr [rax + 8], rbx
00779A67  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00779A6B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00779A6F  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
00779A73  55                              push rbp
00779A74  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00779A78  48 81 EC D0 00 00 00            sub rsp, 0xd0
00779A7F  48 8B 05 BA 0C 69 00            mov rax, qword ptr [rip + 0x690cba]
00779A86  48 33 C4                        xor rax, rsp
00779A89  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00779A8D  83 3D 34 EE 85 00 05            cmp dword ptr [rip + 0x85ee34], 5
00779A94  41 8B D9                        mov ebx, r9d
00779A97  49 8B F8                        mov rdi, r8
00779A9A  8B F2                           mov esi, edx
00779A9C  44 8B F1                        mov r14d, ecx
00779A9F  0F 86 BD 00 00 00               jbe 0x140779b62
00779AA5  BA 01 00 00 00                  mov edx, 1
00779AAA  48 8D 0D 17 EE 85 00            lea rcx, [rip + 0x85ee17]
00779AB1  E8 EA 4F CB FF                  call 0x14042eaa0
00779AB6  84 C0                           test al, al
00779AB8  0F 84 A4 00 00 00               je 0x140779b62
00779ABE  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779AC7  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00779ACE  E8 1D 5E AB FF                  call 0x14022f8f0
00779AD3  83 65 03 00                     and dword ptr [rbp + 3], 0
00779AD7  48 8D 0D EA ED 85 00            lea rcx, [rip + 0x85edea]
00779ADE  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00779AE2  BA 04 00 00 00                  mov edx, 4
00779AE7  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00779AEB  45 33 C9                        xor r9d, r9d
00779AEE  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00779AF2  45 33 C0                        xor r8d, r8d
00779AF5  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00779AF9  89 45 B7                        mov dword ptr [rbp - 0x49], eax
00779AFC  48 8D 45 B7                     lea rax, [rbp - 0x49]
00779B00  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00779B04  48 8D 45 BB                     lea rax, [rbp - 0x45]
00779B08  48 89 45 07                     mov qword ptr [rbp + 7], rax
00779B0C  48 8D 45 BF                     lea rax, [rbp - 0x41]
00779B10  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00779B14  48 8D 45 C7                     lea rax, [rbp - 0x39]
00779B18  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00779B1C  48 8D 45 C3                     lea rax, [rbp - 0x3d]
00779B20  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00779B24  48 8D 45 D7                     lea rax, [rbp - 0x29]
00779B28  89 55 FF                        mov dword ptr [rbp - 1], edx
00779B2B  89 55 0F                        mov dword ptr [rbp + 0xf], edx
00779B2E  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
00779B31  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
00779B34  48 8D 15 DB 8A 8D FF            lea rdx, [rip - 0x727525]
00779B3B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00779B40  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
00779B48  44 89 75 BB                     mov dword ptr [rbp - 0x45], r14d
00779B4C  89 75 BF                        mov dword ptr [rbp - 0x41], esi
00779B4F  48 89 7D C7                     mov qword ptr [rbp - 0x39], rdi
00779B53  C7 45 2F 08 00 00 00            mov dword ptr [rbp + 0x2f], 8
00779B5A  89 5D C3                        mov dword ptr [rbp - 0x3d], ebx
00779B5D  E8 7E C5 CA FF                  call 0x1404260e0
00779B62  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00779B66  48 33 CC                        xor rcx, rsp
00779B69  E8 D2 2A F3 FF                  call 0x1406ac640
00779B6E  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
00779B76  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00779B7A  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00779B7E  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
00779B82  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
00779B86  49 8B E3                        mov rsp, r11
00779B89  5D                              pop rbp
00779B8A  C3                              ret
00779B8B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceFromTerminalRemoved(int a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 6884538)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8777268)) <= 5) goto loc_00779B62;
    result = tlgKeywordOn(v_rip + 8777239, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8777194;
        a2 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 - 73) = (unsigned int)(result);
        result = v_rsp - 95 - 73;
        *(unsigned __int64 *)(v_rsp - 95 - 9) = result;
        result = v_rsp - 95 - 69;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 - 65;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 - 57;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 - 61;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 41;
        *(unsigned int *)(v_rsp - 95 - 1) = a2;
        *(unsigned int *)(v_rsp - 95 + 15) = a2;
        *(unsigned int *)(v_rsp - 95 + 31) = a2;
        *(unsigned int *)(v_rsp - 95 + 63) = a2;
        a2 = v_rip - 7501093;
        v_stack_mB0 = result;
        v_stack_mB8 = 7;
        *(unsigned int *)(v_rsp - 95 - 69) = (unsigned int)((unsigned int)(a1));
        *(unsigned int *)(v_rsp - 95 - 65) = (unsigned int)((unsigned int)(a2));
        *(unsigned __int64 *)(v_rsp - 95 - 57) = 0;
        *(unsigned int *)(v_rsp - 95 + 47) = 8;
        *(unsigned int *)(v_rsp - 95 - 61) = (unsigned int)((unsigned int)(a4));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceFromTerminalRemoved(int32_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x690CBA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85EE34)) <= 5) goto loc_00779B62;
    result = tlgKeywordOn(v_rip + 8777239, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8777194;
        Arg2 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F - 0x49) = (uint32_t)(result);
        result = local_rsp - 95 - 73;
        *(uint64_t *)(local_rsp - 0x5F - 0x9) = result;
        result = local_rsp - 95 - 69;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 - 65;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 - 57;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 - 61;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 41;
        *(uint32_t *)(local_rsp - 0x5F - 0x1) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg2;
        Arg2 = v_rip - 7501093;
        v_stack_mB0 = result;
        v_stack_mB8 = 7;
        *(uint32_t *)(local_rsp - 0x5F - 0x45) = (uint32_t)((uint32_t)(Arg1));
        *(uint32_t *)(local_rsp - 0x5F - 0x41) = (uint32_t)((uint32_t)(Arg2));
        *(uint64_t *)(local_rsp - 0x5F - 0x39) = 0;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = 8;
        *(uint32_t *)(local_rsp - 0x5F - 0x3D) = (uint32_t)((uint32_t)(Arg4));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779A60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779A60[BB_00779A60]
  bb_00779AA5[BB_00779AA5]
  bb_00779ABE[BB_00779ABE]
  bb_00779B62[BB_00779B62]
  bb_00779B8B[BB_00779B8B]
  bb_00779A60 -->|branch| bb_00779B62
  bb_00779A60 -->|fallthrough| bb_00779AA5
  bb_00779AA5 -->|branch| bb_00779B62
  bb_00779AA5 -->|fallthrough| bb_00779ABE
  bb_00779ABE -->|flow| bb_00779B62
```
