# TtmiLogDisplayPowerRequestSet

- RVA: `0x0077A058`–`0x0077A17F` (길이 `295` bytes)
- VA: `0x000000014077A058`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD9C`
- 디코드: `71`개 명령, `295/295` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077A0A9` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077A0C6` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0077A150` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077A15C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiSetDisplayPowerRequest](TtmiSetDisplayPowerRequest_function_0077727C.md) at `0x00777497`

### Static image references
- `0x0077A077` → RVA `0x00E0A740` (`.data`; read)
- `0x0077A085` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077A12F` → RVA `0x00051FFD` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077A0A9` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077A0C6` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0077A150` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077A15C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077A058  48 8B C4                        mov rax, rsp
0077A05B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0077A05F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0077A063  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0077A067  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
0077A06B  55                              push rbp
0077A06C  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0077A070  48 81 EC D0 00 00 00            sub rsp, 0xd0
0077A077  48 8B 05 C2 06 69 00            mov rax, qword ptr [rip + 0x6906c2]
0077A07E  48 33 C4                        xor rax, rsp
0077A081  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077A085  83 3D 3C E8 85 00 05            cmp dword ptr [rip + 0x85e83c], 5
0077A08C  41 8B D9                        mov ebx, r9d
0077A08F  41 8B F8                        mov edi, r8d
0077A092  8B F2                           mov esi, edx
0077A094  44 8B F1                        mov r14d, ecx
0077A097  0F 86 B8 00 00 00               jbe 0x14077a155
0077A09D  BA 01 00 00 00                  mov edx, 1
0077A0A2  48 8D 0D 1F E8 85 00            lea rcx, [rip + 0x85e81f]
0077A0A9  E8 F2 49 CB FF                  call 0x14042eaa0
0077A0AE  84 C0                           test al, al
0077A0B0  0F 84 9F 00 00 00               je 0x14077a155
0077A0B6  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077A0BF  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077A0C6  E8 25 58 AB FF                  call 0x14022f8f0
0077A0CB  83 65 03 00                     and dword ptr [rbp + 3], 0
0077A0CF  48 8D 0D F2 E7 85 00            lea rcx, [rip + 0x85e7f2]
0077A0D6  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0077A0DA  BA 04 00 00 00                  mov edx, 4
0077A0DF  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0077A0E3  45 33 C9                        xor r9d, r9d
0077A0E6  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077A0EA  45 33 C0                        xor r8d, r8d
0077A0ED  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0077A0F1  89 45 B7                        mov dword ptr [rbp - 0x49], eax
0077A0F4  48 8D 45 B7                     lea rax, [rbp - 0x49]
0077A0F8  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0077A0FC  48 8D 45 BB                     lea rax, [rbp - 0x45]
0077A100  48 89 45 07                     mov qword ptr [rbp + 7], rax
0077A104  48 8D 45 BF                     lea rax, [rbp - 0x41]
0077A108  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077A10C  48 8D 45 C3                     lea rax, [rbp - 0x3d]
0077A110  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077A114  48 8D 45 C7                     lea rax, [rbp - 0x39]
0077A118  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077A11C  48 8D 45 D7                     lea rax, [rbp - 0x29]
0077A120  89 55 FF                        mov dword ptr [rbp - 1], edx
0077A123  89 55 0F                        mov dword ptr [rbp + 0xf], edx
0077A126  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0077A129  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0077A12C  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0077A12F  48 8D 15 C7 7E 8D FF            lea rdx, [rip - 0x728139]
0077A136  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077A13B  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
0077A143  44 89 75 BB                     mov dword ptr [rbp - 0x45], r14d
0077A147  89 75 BF                        mov dword ptr [rbp - 0x41], esi
0077A14A  89 7D C3                        mov dword ptr [rbp - 0x3d], edi
0077A14D  89 5D C7                        mov dword ptr [rbp - 0x39], ebx
0077A150  E8 8B BF CA FF                  call 0x1404260e0
0077A155  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077A159  48 33 CC                        xor rcx, rsp
0077A15C  E8 DF 24 F3 FF                  call 0x1406ac640
0077A161  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
0077A169  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0077A16D  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
0077A171  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
0077A175  4D 8B 73 28                     mov r14, qword ptr [r11 + 0x28]
0077A179  49 8B E3                        mov rsp, r11
0077A17C  5D                              pop rbp
0077A17D  C3                              ret
0077A17E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDisplayPowerRequestSet(int a1, int a2, int a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 6883010)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8775740)) <= 5) goto loc_0077A155;
    result = tlgKeywordOn(v_rip + 8775711, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8775666;
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
        result = v_rsp - 95 - 61;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 - 57;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 41;
        *(unsigned int *)(v_rsp - 95 - 1) = a2;
        *(unsigned int *)(v_rsp - 95 + 15) = a2;
        *(unsigned int *)(v_rsp - 95 + 31) = a2;
        *(unsigned int *)(v_rsp - 95 + 47) = a2;
        *(unsigned int *)(v_rsp - 95 + 63) = a2;
        a2 = v_rip - 7504185;
        v_stack_mB0 = result;
        v_stack_mB8 = 7;
        *(unsigned int *)(v_rsp - 95 - 69) = (unsigned int)((unsigned int)(a1));
        *(unsigned int *)(v_rsp - 95 - 65) = (unsigned int)((unsigned int)(a2));
        *(unsigned int *)(v_rsp - 95 - 61) = (unsigned int)((unsigned int)(a3));
        *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)((unsigned int)(a4));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDisplayPowerRequestSet(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x6906C2)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85E83C)) <= 5) goto loc_0077A155;
    result = tlgKeywordOn(v_rip + 8775711, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8775666;
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
        result = local_rsp - 95 - 61;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 - 57;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 41;
        *(uint32_t *)(local_rsp - 0x5F - 0x1) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg2;
        Arg2 = v_rip - 7504185;
        v_stack_mB0 = result;
        v_stack_mB8 = 7;
        *(uint32_t *)(local_rsp - 0x5F - 0x45) = (uint32_t)((uint32_t)(Arg1));
        *(uint32_t *)(local_rsp - 0x5F - 0x41) = (uint32_t)((uint32_t)(Arg2));
        *(uint32_t *)(local_rsp - 0x5F - 0x3D) = (uint32_t)((uint32_t)(Arg3));
        *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)((uint32_t)(Arg4));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077A058&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077A058[BB_0077A058]
  bb_0077A09D[BB_0077A09D]
  bb_0077A0B6[BB_0077A0B6]
  bb_0077A155[BB_0077A155]
  bb_0077A17E[BB_0077A17E]
  bb_0077A058 -->|branch| bb_0077A155
  bb_0077A058 -->|fallthrough| bb_0077A09D
  bb_0077A09D -->|branch| bb_0077A155
  bb_0077A09D -->|fallthrough| bb_0077A0B6
  bb_0077A0B6 -->|flow| bb_0077A155
```
