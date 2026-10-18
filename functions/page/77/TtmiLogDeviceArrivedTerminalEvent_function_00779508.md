# TtmiLogDeviceArrivedTerminalEvent

- RVA: `0x00779508`–`0x0077963F` (길이 `311` bytes)
- VA: `0x0000000140779508`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDDC4`
- 디코드: `77`개 명령, `311/311` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077955D` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077957A` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x007795E6` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (function, `0x00426198`)
- `0x00779610` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077961C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpPublishDeviceEvent](TtmpPublishDeviceEvent_function_00776718.md) at `0x007767ED`

### Static image references
- `0x00779527` → RVA `0x00E0A740` (`.data`; read)
- `0x00779535` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x007795F7` → RVA `0x00052352` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0077955D` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077957A` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x007795E6` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (`PAGE` → `.text`)
  - `0x00779610` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077961C` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779508  48 8B C4                        mov rax, rsp
0077950B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0077950F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00779513  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00779517  55                              push rbp
00779518  41 56                           push r14
0077951A  41 57                           push r15
0077951C  48 8D 68 A9                     lea rbp, [rax - 0x57]
00779520  48 81 EC E0 00 00 00            sub rsp, 0xe0
00779527  48 8B 05 12 12 69 00            mov rax, qword ptr [rip + 0x691212]
0077952E  48 33 C4                        xor rax, rsp
00779531  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
00779535  83 3D 8C F3 85 00 05            cmp dword ptr [rip + 0x85f38c], 5
0077953C  41 8B D9                        mov ebx, r9d
0077953F  4C 8B 7D 7F                     mov r15, qword ptr [rbp + 0x7f]
00779543  41 8B F8                        mov edi, r8d
00779546  8B F2                           mov esi, edx
00779548  44 8B F1                        mov r14d, ecx
0077954B  0F 86 C4 00 00 00               jbe 0x140779615
00779551  BA 01 00 00 00                  mov edx, 1
00779556  48 8D 0D 6B F3 85 00            lea rcx, [rip + 0x85f36b]
0077955D  E8 3E 55 CB FF                  call 0x14042eaa0
00779562  84 C0                           test al, al
00779564  0F 84 AB 00 00 00               je 0x140779615
0077956A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779573  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077957A  E8 71 63 AB FF                  call 0x14022f8f0
0077957F  83 65 DB 00                     and dword ptr [rbp - 0x25], 0
00779583  48 8D 4D 1F                     lea rcx, [rbp + 0x1f]
00779587  83 65 EB 00                     and dword ptr [rbp - 0x15], 0
0077958B  BA 04 00 00 00                  mov edx, 4
00779590  83 65 FB 00                     and dword ptr [rbp - 5], 0
00779594  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
00779598  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
0077959C  89 45 8F                        mov dword ptr [rbp - 0x71], eax
0077959F  48 8D 45 8F                     lea rax, [rbp - 0x71]
007795A3  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
007795A7  48 8D 45 93                     lea rax, [rbp - 0x6d]
007795AB  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
007795AF  48 8D 45 97                     lea rax, [rbp - 0x69]
007795B3  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
007795B7  48 8D 45 9B                     lea rax, [rbp - 0x65]
007795BB  48 89 45 FF                     mov qword ptr [rbp - 1], rax
007795BF  48 8D 45 9F                     lea rax, [rbp - 0x61]
007795C3  89 55 D7                        mov dword ptr [rbp - 0x29], edx
007795C6  89 55 E7                        mov dword ptr [rbp - 0x19], edx
007795C9  89 55 F7                        mov dword ptr [rbp - 9], edx
007795CC  89 55 07                        mov dword ptr [rbp + 7], edx
007795CF  89 55 17                        mov dword ptr [rbp + 0x17], edx
007795D2  49 8B D7                        mov rdx, r15
007795D5  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
007795D9  44 89 75 93                     mov dword ptr [rbp - 0x6d], r14d
007795DD  89 75 97                        mov dword ptr [rbp - 0x69], esi
007795E0  89 7D 9B                        mov dword ptr [rbp - 0x65], edi
007795E3  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
007795E6  E8 AD CB CA FF                  call 0x140426198
007795EB  4C 8D 4D AF                     lea r9, [rbp - 0x51]
007795EF  45 33 C0                        xor r8d, r8d
007795F2  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
007795F7  48 8D 15 54 8D 8D FF            lea rdx, [rip - 0x7272ac]
007795FE  45 33 C9                        xor r9d, r9d
00779601  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
00779609  48 8D 0D B8 F2 85 00            lea rcx, [rip + 0x85f2b8]
00779610  E8 CB CA CA FF                  call 0x1404260e0
00779615  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
00779619  48 33 CC                        xor rcx, rsp
0077961C  E8 1F 30 F3 FF                  call 0x1406ac640
00779621  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00779629  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
0077962D  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
00779631  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
00779635  49 8B E3                        mov rsp, r11
00779638  41 5F                           pop r15
0077963A  41 5E                           pop r14
0077963C  5D                              pop rbp
0077963D  C3                              ret
0077963E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceArrivedTerminalEvent(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (224);
    result = (*(unsigned __int64 *)(v_rip + 6885906)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 47) = result;
    if ((*(unsigned int *)(v_rip + 8778636)) <= 5) goto loc_00779615;
    result = tlgKeywordOn(v_rip + 8778603, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rsp - 87 + 31;
        a2 = 4;
        *(unsigned int *)(v_rsp - 87 - 113) = (unsigned int)(result);
        result = v_rsp - 87 - 113;
        *(unsigned __int64 *)(v_rsp - 87 - 49) = result;
        result = v_rsp - 87 - 109;
        *(unsigned __int64 *)(v_rsp - 87 - 33) = result;
        result = v_rsp - 87 - 105;
        *(unsigned __int64 *)(v_rsp - 87 - 17) = result;
        result = v_rsp - 87 - 101;
        *(unsigned __int64 *)(v_rsp - 87 - 1) = result;
        result = v_rsp - 87 - 97;
        *(unsigned int *)(v_rsp - 87 - 41) = a2;
        *(unsigned int *)(v_rsp - 87 - 25) = a2;
        *(unsigned int *)(v_rsp - 87 - 9) = a2;
        *(unsigned int *)(v_rsp - 87 + 7) = a2;
        *(unsigned int *)(v_rsp - 87 + 23) = a2;
        a2 = *(unsigned __int64 *)(v_rsp - 87 + 127);
        *(unsigned __int64 *)(v_rsp - 87 + 15) = result;
        *(unsigned int *)(v_rsp - 87 - 109) = (unsigned int)((unsigned int)(a1));
        *(unsigned int *)(v_rsp - 87 - 105) = (unsigned int)((unsigned int)(a2));
        *(unsigned int *)(v_rsp - 87 - 101) = (unsigned int)((unsigned int)(a3));
        *(unsigned int *)(v_rsp - 87 - 97) = (unsigned int)((unsigned int)(a4));
        result = tlgCreate1Sz_wchar_t(a1, a2, a3, a4);
        a4 = v_rsp - 87 - 81;
        a3 = 0;
        v_stack_mD0 = a4;
        a2 = v_rip - 7500460;
        a4 = 0;
        v_stack_mD8 = 8;
        a1 = v_rip + 8778424;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 87 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceArrivedTerminalEvent(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (224);
    result = (*(uint64_t *)(v_rip + 0x691212)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x2F) = result;
    if ((*(uint32_t *)(v_rip + 0x85F38C)) <= 5) goto loc_00779615;
    result = tlgKeywordOn(v_rip + 8778603, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = local_rsp - 87 + 31;
        Arg2 = 4;
        *(uint32_t *)(local_rsp - 0x57 - 0x71) = (uint32_t)(result);
        result = local_rsp - 87 - 113;
        *(uint64_t *)(local_rsp - 0x57 - 0x31) = result;
        result = local_rsp - 87 - 109;
        *(uint64_t *)(local_rsp - 0x57 - 0x21) = result;
        result = local_rsp - 87 - 105;
        *(uint64_t *)(local_rsp - 0x57 - 0x11) = result;
        result = local_rsp - 87 - 101;
        *(uint64_t *)(local_rsp - 0x57 - 0x1) = result;
        result = local_rsp - 87 - 97;
        *(uint32_t *)(local_rsp - 0x57 - 0x29) = Arg2;
        *(uint32_t *)(local_rsp - 0x57 - 0x19) = Arg2;
        *(uint32_t *)(local_rsp - 0x57 - 0x9) = Arg2;
        *(uint32_t *)(local_rsp - 0x57 + 0x7) = Arg2;
        *(uint32_t *)(local_rsp - 0x57 + 0x17) = Arg2;
        Arg2 = *(uint64_t *)(local_rsp - 0x57 + 0x7F);
        *(uint64_t *)(local_rsp - 0x57 + 0xF) = result;
        *(uint32_t *)(local_rsp - 0x57 - 0x6D) = (uint32_t)((uint32_t)(Arg1));
        *(uint32_t *)(local_rsp - 0x57 - 0x69) = (uint32_t)((uint32_t)(Arg2));
        *(uint32_t *)(local_rsp - 0x57 - 0x65) = (uint32_t)((uint32_t)(Arg3));
        *(uint32_t *)(local_rsp - 0x57 - 0x61) = (uint32_t)((uint32_t)(Arg4));
        result = tlgCreate1Sz_wchar_t(Arg1, Arg2, Arg3, Arg4);
        Arg4 = local_rsp - 87 - 81;
        Arg3 = 0;
        v_stack_mD0 = Arg4;
        Arg2 = v_rip - 7500460;
        Arg4 = 0;
        v_stack_mD8 = 8;
        Arg1 = v_rip + 8778424;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779508&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779508[BB_00779508]
  bb_00779551[BB_00779551]
  bb_0077956A[BB_0077956A]
  bb_00779615[BB_00779615]
  bb_0077963E[BB_0077963E]
  bb_00779508 -->|branch| bb_00779615
  bb_00779508 -->|fallthrough| bb_00779551
  bb_00779551 -->|branch| bb_00779615
  bb_00779551 -->|fallthrough| bb_0077956A
  bb_0077956A -->|flow| bb_00779615
```
