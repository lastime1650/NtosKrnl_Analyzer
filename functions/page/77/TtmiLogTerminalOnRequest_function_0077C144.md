# TtmiLogTerminalOnRequest

- RVA: `0x0077C144`–`0x0077C255` (길이 `273` bytes)
- VA: `0x000000014077C144`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD2C`
- 디코드: `64`개 명령, `273/273` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077C18A` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077C1A7` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0077C22E` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077C23A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiSetPendingOnOffRequest](TtmiSetPendingOnOffRequest_function_0077D074.md) at `0x0077D0E7`

### Static image references
- `0x0077C15F` → RVA `0x00E0A740` (`.data`; read)
- `0x0077C16D` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077C20D` → RVA `0x00051304` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077C18A` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077C1A7` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0077C22E` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077C23A` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077C144  48 8B C4                        mov rax, rsp
0077C147  48 89 58 08                     mov qword ptr [rax + 8], rbx
0077C14B  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0077C14F  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0077C153  55                              push rbp
0077C154  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0077C158  48 81 EC C0 00 00 00            sub rsp, 0xc0
0077C15F  48 8B 05 DA E5 68 00            mov rax, qword ptr [rip + 0x68e5da]
0077C166  48 33 C4                        xor rax, rsp
0077C169  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077C16D  83 3D 54 C7 85 00 05            cmp dword ptr [rip + 0x85c754], 5
0077C174  8B DA                           mov ebx, edx
0077C176  8B F9                           mov edi, ecx
0077C178  0F 86 B5 00 00 00               jbe 0x14077c233
0077C17E  BA 01 00 00 00                  mov edx, 1
0077C183  48 8D 0D 3E C7 85 00            lea rcx, [rip + 0x85c73e]
0077C18A  E8 11 29 CB FF                  call 0x14042eaa0
0077C18F  84 C0                           test al, al
0077C191  0F 84 9C 00 00 00               je 0x14077c233
0077C197  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077C1A0  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077C1A7  E8 44 37 AB FF                  call 0x14022f8f0
0077C1AC  83 65 03 00                     and dword ptr [rbp + 3], 0
0077C1B0  48 8D 0D 11 C7 85 00            lea rcx, [rip + 0x85c711]
0077C1B7  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0077C1BB  BA 04 00 00 00                  mov edx, 4
0077C1C0  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0077C1C4  45 33 C9                        xor r9d, r9d
0077C1C7  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077C1CB  45 33 C0                        xor r8d, r8d
0077C1CE  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0077C1D2  89 45 C7                        mov dword ptr [rbp - 0x39], eax
0077C1D5  48 8D 45 C7                     lea rax, [rbp - 0x39]
0077C1D9  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0077C1DD  48 8D 45 CB                     lea rax, [rbp - 0x35]
0077C1E1  48 89 45 07                     mov qword ptr [rbp + 7], rax
0077C1E5  48 8D 45 CF                     lea rax, [rbp - 0x31]
0077C1E9  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077C1ED  48 8D 45 3F                     lea rax, [rbp + 0x3f]
0077C1F1  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077C1F5  48 8D 45 77                     lea rax, [rbp + 0x77]
0077C1F9  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077C1FD  48 8D 45 D7                     lea rax, [rbp - 0x29]
0077C201  89 55 FF                        mov dword ptr [rbp - 1], edx
0077C204  89 55 0F                        mov dword ptr [rbp + 0xf], edx
0077C207  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0077C20A  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0077C20D  48 8D 15 F0 50 8D FF            lea rdx, [rip - 0x72af10]
0077C214  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077C219  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
0077C221  89 7D CB                        mov dword ptr [rbp - 0x35], edi
0077C224  89 5D CF                        mov dword ptr [rbp - 0x31], ebx
0077C227  C7 45 2F 02 00 00 00            mov dword ptr [rbp + 0x2f], 2
0077C22E  E8 AD 9E CA FF                  call 0x1404260e0
0077C233  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077C237  48 33 CC                        xor rcx, rsp
0077C23A  E8 01 04 F3 FF                  call 0x1406ac640
0077C23F  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
0077C247  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0077C24B  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
0077C24F  49 8B E3                        mov rsp, r11
0077C252  5D                              pop rbp
0077C253  C3                              ret
0077C254  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalOnRequest(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rdi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 6874586)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8767316)) <= 5) goto loc_0077C233;
    result = tlgKeywordOn(v_rip + 8767294, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8767249;
        a2 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 - 57) = (unsigned int)(result);
        result = v_rsp - 95 - 57;
        *(unsigned __int64 *)(v_rsp - 95 - 9) = result;
        result = v_rsp - 95 - 53;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 - 49;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 63;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 + 119;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 41;
        *(unsigned int *)(v_rsp - 95 - 1) = a2;
        *(unsigned int *)(v_rsp - 95 + 15) = a2;
        *(unsigned int *)(v_rsp - 95 + 31) = a2;
        *(unsigned int *)(v_rsp - 95 + 63) = a2;
        a2 = v_rip - 7515920;
        v_stack_mA0 = result;
        v_stack_mA8 = 7;
        *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)((unsigned int)(a1));
        *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(a2));
        *(unsigned int *)(v_rsp - 95 + 47) = 2;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogTerminalOnRequest(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rdi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x68E5DA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85C754)) <= 5) goto loc_0077C233;
    result = tlgKeywordOn(v_rip + 8767294, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8767249;
        Arg2 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F - 0x39) = (uint32_t)(result);
        result = local_rsp - 95 - 57;
        *(uint64_t *)(local_rsp - 0x5F - 0x9) = result;
        result = local_rsp - 95 - 53;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 - 49;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 63;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 + 119;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 41;
        *(uint32_t *)(local_rsp - 0x5F - 0x1) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg2;
        Arg2 = v_rip - 7515920;
        v_stack_mA0 = result;
        v_stack_mA8 = 7;
        *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)((uint32_t)(Arg1));
        *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(Arg2));
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = 2;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077C144&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077C144[BB_0077C144]
  bb_0077C17E[BB_0077C17E]
  bb_0077C197[BB_0077C197]
  bb_0077C233[BB_0077C233]
  bb_0077C254[BB_0077C254]
  bb_0077C144 -->|branch| bb_0077C233
  bb_0077C144 -->|fallthrough| bb_0077C17E
  bb_0077C17E -->|branch| bb_0077C233
  bb_0077C17E -->|fallthrough| bb_0077C197
  bb_0077C197 -->|flow| bb_0077C233
```
