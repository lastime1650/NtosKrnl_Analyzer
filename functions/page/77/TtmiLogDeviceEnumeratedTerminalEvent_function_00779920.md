# TtmiLogDeviceEnumeratedTerminalEvent

- RVA: `0x00779920`–`0x00779A57` (길이 `311` bytes)
- VA: `0x0000000140779920`
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
- `0x00779975` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00779992` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x007799FE` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (function, `0x00426198`)
- `0x00779A28` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00779A34` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpPublishDeviceEvent](TtmpPublishDeviceEvent_function_00776718.md) at `0x007767E6`

### Static image references
- `0x0077993F` → RVA `0x00E0A740` (`.data`; read)
- `0x0077994D` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00779A0F` → RVA `0x00052591` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00779975` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00779992` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x007799FE` → [tlgCreate1Sz_wchar_t](../../text/42/tlgCreate1Sz_wchar_t_function_00426198.md) (`PAGE` → `.text`)
  - `0x00779A28` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00779A34` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779920  48 8B C4                        mov rax, rsp
00779923  48 89 58 08                     mov qword ptr [rax + 8], rbx
00779927  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
0077992B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
0077992F  55                              push rbp
00779930  41 56                           push r14
00779932  41 57                           push r15
00779934  48 8D 68 A9                     lea rbp, [rax - 0x57]
00779938  48 81 EC E0 00 00 00            sub rsp, 0xe0
0077993F  48 8B 05 FA 0D 69 00            mov rax, qword ptr [rip + 0x690dfa]
00779946  48 33 C4                        xor rax, rsp
00779949  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
0077994D  83 3D 74 EF 85 00 05            cmp dword ptr [rip + 0x85ef74], 5
00779954  41 8B D9                        mov ebx, r9d
00779957  4C 8B 7D 7F                     mov r15, qword ptr [rbp + 0x7f]
0077995B  41 8B F8                        mov edi, r8d
0077995E  8B F2                           mov esi, edx
00779960  44 8B F1                        mov r14d, ecx
00779963  0F 86 C4 00 00 00               jbe 0x140779a2d
00779969  BA 01 00 00 00                  mov edx, 1
0077996E  48 8D 0D 53 EF 85 00            lea rcx, [rip + 0x85ef53]
00779975  E8 26 51 CB FF                  call 0x14042eaa0
0077997A  84 C0                           test al, al
0077997C  0F 84 AB 00 00 00               je 0x140779a2d
00779982  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077998B  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00779992  E8 59 5F AB FF                  call 0x14022f8f0
00779997  83 65 DB 00                     and dword ptr [rbp - 0x25], 0
0077999B  48 8D 4D 1F                     lea rcx, [rbp + 0x1f]
0077999F  83 65 EB 00                     and dword ptr [rbp - 0x15], 0
007799A3  BA 04 00 00 00                  mov edx, 4
007799A8  83 65 FB 00                     and dword ptr [rbp - 5], 0
007799AC  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
007799B0  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
007799B4  89 45 8F                        mov dword ptr [rbp - 0x71], eax
007799B7  48 8D 45 8F                     lea rax, [rbp - 0x71]
007799BB  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
007799BF  48 8D 45 93                     lea rax, [rbp - 0x6d]
007799C3  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
007799C7  48 8D 45 97                     lea rax, [rbp - 0x69]
007799CB  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
007799CF  48 8D 45 9B                     lea rax, [rbp - 0x65]
007799D3  48 89 45 FF                     mov qword ptr [rbp - 1], rax
007799D7  48 8D 45 9F                     lea rax, [rbp - 0x61]
007799DB  89 55 D7                        mov dword ptr [rbp - 0x29], edx
007799DE  89 55 E7                        mov dword ptr [rbp - 0x19], edx
007799E1  89 55 F7                        mov dword ptr [rbp - 9], edx
007799E4  89 55 07                        mov dword ptr [rbp + 7], edx
007799E7  89 55 17                        mov dword ptr [rbp + 0x17], edx
007799EA  49 8B D7                        mov rdx, r15
007799ED  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
007799F1  44 89 75 93                     mov dword ptr [rbp - 0x6d], r14d
007799F5  89 75 97                        mov dword ptr [rbp - 0x69], esi
007799F8  89 7D 9B                        mov dword ptr [rbp - 0x65], edi
007799FB  89 5D 9F                        mov dword ptr [rbp - 0x61], ebx
007799FE  E8 95 C7 CA FF                  call 0x140426198
00779A03  4C 8D 4D AF                     lea r9, [rbp - 0x51]
00779A07  45 33 C0                        xor r8d, r8d
00779A0A  4C 89 4C 24 28                  mov qword ptr [rsp + 0x28], r9
00779A0F  48 8D 15 7B 8B 8D FF            lea rdx, [rip - 0x727485]
00779A16  45 33 C9                        xor r9d, r9d
00779A19  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
00779A21  48 8D 0D A0 EE 85 00            lea rcx, [rip + 0x85eea0]
00779A28  E8 B3 C6 CA FF                  call 0x1404260e0
00779A2D  48 8B 4D 2F                     mov rcx, qword ptr [rbp + 0x2f]
00779A31  48 33 CC                        xor rcx, rsp
00779A34  E8 07 2C F3 FF                  call 0x1406ac640
00779A39  4C 8D 9C 24 E0 00 00 00         lea r11, [rsp + 0xe0]
00779A41  49 8B 5B 20                     mov rbx, qword ptr [r11 + 0x20]
00779A45  49 8B 73 28                     mov rsi, qword ptr [r11 + 0x28]
00779A49  49 8B 7B 30                     mov rdi, qword ptr [r11 + 0x30]
00779A4D  49 8B E3                        mov rsp, r11
00779A50  41 5F                           pop r15
00779A52  41 5E                           pop r14
00779A54  5D                              pop rbp
00779A55  C3                              ret
00779A56  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceEnumeratedTerminalEvent(int a1, int a2, int a3, int a4)
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
    result = (*(unsigned __int64 *)(v_rip + 6884858)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 47) = result;
    if ((*(unsigned int *)(v_rip + 8777588)) <= 5) goto loc_00779A2D;
    result = tlgKeywordOn(v_rip + 8777555, 1, a3, a4);
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
        a2 = v_rip - 7500933;
        a4 = 0;
        v_stack_mD8 = 8;
        a1 = v_rip + 8777376;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 87 + 47)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceEnumeratedTerminalEvent(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
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
    result = (*(uint64_t *)(v_rip + 0x690DFA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x2F) = result;
    if ((*(uint32_t *)(v_rip + 0x85EF74)) <= 5) goto loc_00779A2D;
    result = tlgKeywordOn(v_rip + 8777555, 1, Arg3, Arg4);
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
        Arg2 = v_rip - 7500933;
        Arg4 = 0;
        v_stack_mD8 = 8;
        Arg1 = v_rip + 8777376;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x2F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779920[BB_00779920]
  bb_00779969[BB_00779969]
  bb_00779982[BB_00779982]
  bb_00779A2D[BB_00779A2D]
  bb_00779A56[BB_00779A56]
  bb_00779920 -->|branch| bb_00779A2D
  bb_00779920 -->|fallthrough| bb_00779969
  bb_00779969 -->|branch| bb_00779A2D
  bb_00779969 -->|fallthrough| bb_00779982
  bb_00779982 -->|flow| bb_00779A2D
```
