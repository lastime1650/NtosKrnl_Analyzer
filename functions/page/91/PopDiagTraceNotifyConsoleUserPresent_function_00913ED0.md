# PopDiagTraceNotifyConsoleUserPresent

- RVA: `0x00913ED0`–`0x00913FAC` (길이 `220` bytes)
- VA: `0x0000000140913ED0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A558`
- 디코드: `53`개 명령, `220/220` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00913F19` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00913F89` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00913F95` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopNotifyConsoleUserPresent](PopNotifyConsoleUserPresent_function_00913C50.md) at `0x00913E78`

### Static image references
- `0x00913EED` → RVA `0x00E0A740` (`.data`; read)
- `0x00913EFB` → RVA `0x00E67858` (`.data`; read)
- `0x00913F0B` → RVA `0x00F0B408` (`.data`; read)
- `0x00913F12` → RVA `0x00011AE8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00913F19` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00913F89` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00913F95` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00913ED0  48 8B C4                        mov rax, rsp
00913ED3  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00913ED7  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00913EDB  89 50 10                        mov dword ptr [rax + 0x10], edx
00913EDE  88 48 08                        mov byte ptr [rax + 8], cl
00913EE1  55                              push rbp
00913EE2  48 8D 68 A1                     lea rbp, [rax - 0x5f]
00913EE6  48 81 EC 90 00 00 00            sub rsp, 0x90
00913EED  48 8B 05 4C 68 4F 00            mov rax, qword ptr [rip + 0x4f684c]
00913EF4  48 33 C4                        xor rax, rsp
00913EF7  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00913EFB  80 3D 56 39 55 00 00            cmp byte ptr [rip + 0x553956], 0
00913F02  41 8A D8                        mov bl, r8b
00913F05  0F 84 83 00 00 00               je 0x140913f8e
00913F0B  48 8B 0D F6 74 5F 00            mov rcx, qword ptr [rip + 0x5f74f6]
00913F12  48 8D 15 CF DB 6F FF            lea rdx, [rip - 0x902431]
00913F19  E8 32 E5 A7 FF                  call 0x140392450
00913F1E  84 C0                           test al, al
00913F20  74 6C                           je 0x140913f8e
00913F22  B9 01 00 00 00                  mov ecx, 1
00913F27  48 8D 45 67                     lea rax, [rbp + 0x67]
00913F2B  48 89 45 07                     mov qword ptr [rbp + 7], rax
00913F2F  48 8D 15 B2 DB 6F FF            lea rdx, [rip - 0x90244e]
00913F36  48 8D 45 F7                     lea rax, [rbp - 9]
00913F3A  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
00913F3D  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00913F41  84 DB                           test bl, bl
00913F43  44 8D 49 03                     lea r9d, [rcx + 3]
00913F47  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
00913F4A  48 8B 0D B7 74 5F 00            mov rcx, qword ptr [rip + 0x5f74b7]
00913F51  48 8D 45 6F                     lea rax, [rbp + 0x6f]
00913F55  0F 95 45 F7                     setne byte ptr [rbp - 9]
00913F59  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00913F5D  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00913F61  48 8D 45 7F                     lea rax, [rbp + 0x7f]
00913F65  83 65 23 00                     and dword ptr [rbp + 0x23], 0
00913F69  45 33 C0                        xor r8d, r8d
00913F6C  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00913F70  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00913F74  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00913F78  48 8D 45 07                     lea rax, [rbp + 7]
00913F7C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00913F81  44 89 4D 2F                     mov dword ptr [rbp + 0x2f], r9d
00913F85  44 89 4D 3F                     mov dword ptr [rbp + 0x3f], r9d
00913F89  E8 92 87 B0 FF                  call 0x14041c720
00913F8E  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00913F92  48 33 CC                        xor rcx, rsp
00913F95  E8 A6 86 D9 FF                  call 0x1406ac640
00913F9A  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00913FA2  48 81 C4 90 00 00 00            add rsp, 0x90
00913FA9  5D                              pop rbp
00913FAA  C3                              ret
00913FAB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceNotifyConsoleUserPresent(unsigned __int8 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int8 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 5204044)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned __int8 *)(v_rip + 5585238)) == 0) goto loc_00913F8E;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6255862), v_rip - 9446449, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = 1;
        result = v_rsp - 95 + 103;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        a2 = v_rip - 9446478;
        result = v_rsp - 95 - 9;
        *(unsigned int *)(v_rsp - 95 + 15) = a1;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        a4 = a1 + 3;
        *(unsigned int *)(v_rsp - 95 + 31) = a1;
        a1 = *(unsigned __int64 *)(v_rip + 6255799);
        result = v_rsp - 95 + 111;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 + 127;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 + 7;
        v_stack_m78 = result;
        *(unsigned int *)(v_rsp - 95 + 47) = a4;
        *(unsigned int *)(v_rsp - 95 + 63) = a4;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceNotifyConsoleUserPresent(uint8_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m78;
    uint64_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint8_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x4F684C)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint8_t *)(v_rip + 0x553956)) == 0) goto loc_00913F8E;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x5F74F6), v_rip - 9446449, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = 1;
        result = local_rsp - 95 + 103;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        Arg2 = v_rip - 9446478;
        result = local_rsp - 95 - 9;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg1;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        Arg4 = Arg1 + 3;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg1;
        Arg1 = *(uint64_t *)(v_rip + 0x5F74B7);
        result = local_rsp - 95 + 111;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 + 127;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 + 7;
        v_stack_m78 = result;
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = Arg4;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg4;
        result = EtwWrite(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00913ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00913ED0[BB_00913ED0]
  bb_00913F0B[BB_00913F0B]
  bb_00913F22[BB_00913F22]
  bb_00913F8E[BB_00913F8E]
  bb_00913FAB[BB_00913FAB]
  bb_00913ED0 -->|branch| bb_00913F8E
  bb_00913ED0 -->|fallthrough| bb_00913F0B
  bb_00913F0B -->|branch| bb_00913F8E
  bb_00913F0B -->|fallthrough| bb_00913F22
  bb_00913F22 -->|flow| bb_00913F8E
```
