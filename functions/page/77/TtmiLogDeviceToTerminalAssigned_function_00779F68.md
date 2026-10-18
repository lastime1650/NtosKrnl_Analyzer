# TtmiLogDeviceToTerminalAssigned

- RVA: `0x00779F68`–`0x0077A04F` (길이 `231` bytes)
- VA: `0x0000000140779F68`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078F20`
- 디코드: `54`개 명령, `231/231` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00779FAA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00779FC3` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0077A028` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077A034` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiAssignDevice](TtmiAssignDevice_function_00775A3C.md) at `0x00775AB7`

### Static image references
- `0x00779F7F` → RVA `0x00E0A740` (`.data`; read)
- `0x00779F8D` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077A00E` → RVA `0x000518F8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00779FAA` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00779FC3` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0077A028` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077A034` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779F68  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00779F6D  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00779F72  55                              push rbp
00779F73  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00779F78  48 81 EC A0 00 00 00            sub rsp, 0xa0
00779F7F  48 8B 05 BA 07 69 00            mov rax, qword ptr [rip + 0x6907ba]
00779F86  48 33 C4                        xor rax, rsp
00779F89  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00779F8D  83 3D 34 E9 85 00 05            cmp dword ptr [rip + 0x85e934], 5
00779F94  8B DA                           mov ebx, edx
00779F96  8B F9                           mov edi, ecx
00779F98  0F 86 8F 00 00 00               jbe 0x14077a02d
00779F9E  BA 01 00 00 00                  mov edx, 1
00779FA3  48 8D 0D 1E E9 85 00            lea rcx, [rip + 0x85e91e]
00779FAA  E8 F1 4A CB FF                  call 0x14042eaa0
00779FAF  84 C0                           test al, al
00779FB1  74 7A                           je 0x14077a02d
00779FB3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00779FBC  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
00779FC3  E8 28 59 AB FF                  call 0x14022f8f0
00779FC8  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00779FCC  48 8D 0D F5 E8 85 00            lea rcx, [rip + 0x85e8f5]
00779FD3  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00779FD7  BA 04 00 00 00                  mov edx, 4
00779FDC  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00779FE0  45 33 C9                        xor r9d, r9d
00779FE3  89 45 E7                        mov dword ptr [rbp - 0x19], eax
00779FE6  45 33 C0                        xor r8d, r8d
00779FE9  48 8D 45 E7                     lea rax, [rbp - 0x19]
00779FED  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
00779FF0  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00779FF4  48 8D 45 EB                     lea rax, [rbp - 0x15]
00779FF8  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00779FFC  48 8D 45 EF                     lea rax, [rbp - 0x11]
0077A000  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077A004  48 8D 45 F7                     lea rax, [rbp - 9]
0077A008  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0077A00B  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0077A00E  48 8D 15 E3 78 8D FF            lea rdx, [rip - 0x72871d]
0077A015  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077A01A  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
0077A022  89 7D EB                        mov dword ptr [rbp - 0x15], edi
0077A025  89 5D EF                        mov dword ptr [rbp - 0x11], ebx
0077A028  E8 B3 C0 CA FF                  call 0x1404260e0
0077A02D  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077A031  48 33 CC                        xor rcx, rsp
0077A034  E8 07 26 F3 FF                  call 0x1406ac640
0077A039  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
0077A041  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0077A045  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
0077A049  49 8B E3                        mov rsp, r11
0077A04C  5D                              pop rbp
0077A04D  C3                              ret
0077A04E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceToTerminalAssigned(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6883258)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8775988)) <= 5) goto loc_0077A02D;
    result = tlgKeywordOn(v_rip + 8775966, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8775925;
        a2 = 4;
        a4 = 0;
        v_stack_m78 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m78;
        v_stack_m40 = a2;
        v_stack_m48 = result;
        result = v_stack_m74;
        v_stack_m38 = result;
        result = v_stack_m70;
        v_stack_m28 = result;
        result = v_stack_m68;
        v_stack_m30 = a2;
        v_stack_m20 = a2;
        a2 = v_rip - 7505693;
        v_stack_m80 = result;
        v_stack_m88 = 5;
        v_stack_m74 = (unsigned int)((unsigned int)(a1));
        v_stack_m70 = (unsigned int)((unsigned int)(a2));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceToTerminalAssigned(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m8;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6907BA)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85E934)) <= 5) goto loc_0077A02D;
    result = tlgKeywordOn(v_rip + 8775966, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8775925;
        Arg2 = 4;
        Arg4 = 0;
        v_stack_m78 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m78;
        v_stack_m40 = Arg2;
        v_stack_m48 = result;
        result = v_stack_m74;
        v_stack_m38 = result;
        result = v_stack_m70;
        v_stack_m28 = result;
        result = v_stack_m68;
        v_stack_m30 = Arg2;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 7505693;
        v_stack_m80 = result;
        v_stack_m88 = 5;
        v_stack_m74 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m70 = (uint32_t)((uint32_t)(Arg2));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779F68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779F68[BB_00779F68]
  bb_00779F9E[BB_00779F9E]
  bb_00779FB3[BB_00779FB3]
  bb_0077A02D[BB_0077A02D]
  bb_0077A04E[BB_0077A04E]
  bb_00779F68 -->|branch| bb_0077A02D
  bb_00779F68 -->|fallthrough| bb_00779F9E
  bb_00779F9E -->|branch| bb_0077A02D
  bb_00779F9E -->|fallthrough| bb_00779FB3
  bb_00779FB3 -->|flow| bb_0077A02D
```
