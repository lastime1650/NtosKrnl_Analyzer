# TtmiLogDeviceSetInputWakeCapability

- RVA: `0x00779E58`–`0x00779F60` (길이 `264` bytes)
- VA: `0x0000000140779E58`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD08`
- 디코드: `63`개 명령, `264/264` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00779EA1` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00779EBE` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00779F35` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00779F41` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiSetInputWakeCapability](TtmiSetInputWakeCapability_function_00775E84.md) at `0x00775EF9`

### Static image references
- `0x00779E73` → RVA `0x00E0A740` (`.data`; read)
- `0x00779E81` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00779F18` → RVA `0x000514E5` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00779EA1` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00779EBE` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00779F35` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00779F41` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779E58  48 8B C4                        mov rax, rsp
00779E5B  48 89 58 08                     mov qword ptr [rax + 8], rbx
00779E5F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00779E63  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00779E67  55                              push rbp
00779E68  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00779E6C  48 81 EC B0 00 00 00            sub rsp, 0xb0
00779E73  48 8B 05 C6 08 69 00            mov rax, qword ptr [rip + 0x6908c6]
00779E7A  48 33 C4                        xor rax, rsp
00779E7D  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00779E81  83 3D 40 EA 85 00 05            cmp dword ptr [rip + 0x85ea40], 5
00779E88  41 8B D8                        mov ebx, r8d
00779E8B  8B FA                           mov edi, edx
00779E8D  8B F1                           mov esi, ecx
00779E8F  0F 86 A5 00 00 00               jbe 0x140779f3a
00779E95  BA 01 00 00 00                  mov edx, 1
00779E9A  48 8D 0D 27 EA 85 00            lea rcx, [rip + 0x85ea27]
00779EA1  E8 FA 4B CB FF                  call 0x14042eaa0
00779EA6  84 C0                           test al, al
00779EA8  0F 84 8C 00 00 00               je 0x140779f3a
00779EAE  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779EB7  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00779EBE  E8 2D 5A AB FF                  call 0x14022f8f0
00779EC3  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00779EC7  48 8D 0D FA E9 85 00            lea rcx, [rip + 0x85e9fa]
00779ECE  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00779ED2  BA 04 00 00 00                  mov edx, 4
00779ED7  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00779EDB  45 33 C9                        xor r9d, r9d
00779EDE  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00779EE2  45 33 C0                        xor r8d, r8d
00779EE5  89 45 D7                        mov dword ptr [rbp - 0x29], eax
00779EE8  48 8D 45 D7                     lea rax, [rbp - 0x29]
00779EEC  48 89 45 07                     mov qword ptr [rbp + 7], rax
00779EF0  48 8D 45 DB                     lea rax, [rbp - 0x25]
00779EF4  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00779EF8  48 8D 45 DF                     lea rax, [rbp - 0x21]
00779EFC  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00779F00  48 8D 45 E3                     lea rax, [rbp - 0x1d]
00779F04  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00779F08  48 8D 45 E7                     lea rax, [rbp - 0x19]
00779F0C  89 55 0F                        mov dword ptr [rbp + 0xf], edx
00779F0F  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
00779F12  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
00779F15  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
00779F18  48 8D 15 C6 75 8D FF            lea rdx, [rip - 0x728a3a]
00779F1F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00779F24  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
00779F2C  89 75 DB                        mov dword ptr [rbp - 0x25], esi
00779F2F  89 7D DF                        mov dword ptr [rbp - 0x21], edi
00779F32  89 5D E3                        mov dword ptr [rbp - 0x1d], ebx
00779F35  E8 A6 C1 CA FF                  call 0x1404260e0
00779F3A  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00779F3E  48 33 CC                        xor rcx, rsp
00779F41  E8 FA 26 F3 FF                  call 0x1406ac640
00779F46  4C 8D 9C 24 B0 00 00 00         lea r11, [rsp + 0xb0]
00779F4E  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00779F52  49 8B 73 18                     mov rsi, qword ptr [r11 + 0x18]
00779F56  49 8B 7B 20                     mov rdi, qword ptr [r11 + 0x20]
00779F5A  49 8B E3                        mov rsp, r11
00779F5D  5D                              pop rbp
00779F5E  C3                              ret
00779F5F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceSetInputWakeCapability(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 6883526)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8776256)) <= 5) goto loc_00779F3A;
    result = tlgKeywordOn(v_rip + 8776231, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8776186;
        a2 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 - 41) = (unsigned int)(result);
        result = v_rsp - 95 - 41;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 - 37;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 - 33;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 - 29;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 25;
        *(unsigned int *)(v_rsp - 95 + 15) = a2;
        *(unsigned int *)(v_rsp - 95 + 31) = a2;
        *(unsigned int *)(v_rsp - 95 + 47) = a2;
        *(unsigned int *)(v_rsp - 95 + 63) = a2;
        a2 = v_rip - 7506490;
        v_stack_m90 = result;
        v_stack_m98 = 6;
        *(unsigned int *)(v_rsp - 95 - 37) = (unsigned int)((unsigned int)(a1));
        *(unsigned int *)(v_rsp - 95 - 33) = (unsigned int)((unsigned int)(a2));
        *(unsigned int *)(v_rsp - 95 - 29) = (unsigned int)((unsigned int)(a3));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceSetInputWakeCapability(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x6908C6)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85EA40)) <= 5) goto loc_00779F3A;
    result = tlgKeywordOn(v_rip + 8776231, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8776186;
        Arg2 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F - 0x29) = (uint32_t)(result);
        result = local_rsp - 95 - 41;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 - 37;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 - 33;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 - 29;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 25;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg2;
        Arg2 = v_rip - 7506490;
        v_stack_m90 = result;
        v_stack_m98 = 6;
        *(uint32_t *)(local_rsp - 0x5F - 0x25) = (uint32_t)((uint32_t)(Arg1));
        *(uint32_t *)(local_rsp - 0x5F - 0x21) = (uint32_t)((uint32_t)(Arg2));
        *(uint32_t *)(local_rsp - 0x5F - 0x1D) = (uint32_t)((uint32_t)(Arg3));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779E58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779E58[BB_00779E58]
  bb_00779E95[BB_00779E95]
  bb_00779EAE[BB_00779EAE]
  bb_00779F3A[BB_00779F3A]
  bb_00779F5F[BB_00779F5F]
  bb_00779E58 -->|branch| bb_00779F3A
  bb_00779E58 -->|fallthrough| bb_00779E95
  bb_00779E95 -->|branch| bb_00779F3A
  bb_00779E95 -->|fallthrough| bb_00779EAE
  bb_00779EAE -->|flow| bb_00779F3A
```
