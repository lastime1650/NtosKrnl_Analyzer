# DifCmRegisterCallbackExWrapper

- RVA: `0x0061C780`–`0x0061C929` (길이 `425` bytes)
- VA: `0x000000014061C780`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `120`개 명령, `425/425` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061C7B6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0061C7C0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061C7E8` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061C834` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C85A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C873` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061C897` → [CmRegisterCallbackEx](../../page/AA/CmRegisterCallbackEx_function_00AAFE70.md) (function, `0x00AAFE70`)
- `0x0061C8C3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C8E9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C902` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061C7F8` → RVA `0x00F048B8` (`.data`; read)
- `0x0061C821` → RVA `0x00F04980` (`.data`; read)
- `0x0061C82D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0061C897` → [CmRegisterCallbackEx](../../page/AA/CmRegisterCallbackEx_function_00AAFE70.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061C780  48 8B C4                        mov rax, rsp
0061C783  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0061C787  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061C78B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061C78F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0061C793  55                              push rbp
0061C794  41 54                           push r12
0061C796  41 55                           push r13
0061C798  41 56                           push r14
0061C79A  41 57                           push r15
0061C79C  48 8B EC                        mov rbp, rsp
0061C79F  48 83 EC 70                     sub rsp, 0x70
0061C7A3  4C 8B EA                        mov r13, rdx
0061C7A6  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0061C7AA  33 D2                           xor edx, edx
0061C7AC  4D 8B E0                        mov r12, r8
0061C7AF  4D 8B F9                        mov r15, r9
0061C7B2  44 8D 42 40                     lea r8d, [rdx + 0x40]
0061C7B6  E8 85 A4 0A 00                  call 0x1406c6c40
0061C7BB  B9 AD 01 00 00                  mov ecx, 0x1ad
0061C7C0  E8 6F 92 E7 FF                  call 0x140495a34
0061C7C5  4C 8B F0                        mov r14, rax
0061C7C8  48 85 C0                        test rax, rax
0061C7CB  0F 84 A7 00 00 00               je 0x14061c878
0061C7D1  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0061C7D4  F6 C1 18                        test cl, 0x18
0061C7D7  74 0A                           je 0x14061c7e3
0061C7D9  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061C7DD  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0061C7E1  EB 0E                           jmp 0x14061c7f1
0061C7E3  F6 C1 04                        test cl, 4
0061C7E6  74 09                           je 0x14061c7f1
0061C7E8  E8 1B 74 EB FF                  call 0x1404d3c08
0061C7ED  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0061C7F1  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0061C7F5  40 32 F6                        xor sil, sil
0061C7F8  40 38 35 B9 80 8E 00            cmp byte ptr [rip + 0x8e80b9], sil
0061C7FF  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061C803  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0061C807  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061C80B  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0061C80F  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0061C813  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0061C817  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0061C81B  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
0061C81F  75 0C                           jne 0x14061c82d
0061C821  F7 05 55 81 8E 00 00 08 00 00   test dword ptr [rip + 0x8e8155], 0x800
0061C82B  74 13                           je 0x14061c840
0061C82D  48 8D 0D 4C 76 8E 00            lea rcx, [rip + 0x8e764c]
0061C834  E8 E7 9D BF FF                  call 0x140216620
0061C839  40 8A F0                        mov sil, al
0061C83C  84 C0                           test al, al
0061C83E  74 38                           je 0x14061c878
0061C840  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0061C844  48 8B 1F                        mov rbx, qword ptr [rdi]
0061C847  EB 19                           jmp 0x14061c862
0061C849  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C84D  48 85 C0                        test rax, rax
0061C850  74 0D                           je 0x14061c85f
0061C852  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C856  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0061C85A  E8 71 E2 09 00                  call 0x1406baad0
0061C85F  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C862  48 3B DF                        cmp rbx, rdi
0061C865  75 E2                           jne 0x14061c849
0061C867  40 84 F6                        test sil, sil
0061C86A  74 0C                           je 0x14061c878
0061C86C  48 8D 0D 0D 76 8E 00            lea rcx, [rip + 0x8e760d]
0061C873  E8 08 D6 D2 FF                  call 0x140349e80
0061C878  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0061C87C  4D 8B CF                        mov r9, r15
0061C87F  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0061C883  4D 8B C4                        mov r8, r12
0061C886  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0061C88B  49 8B D5                        mov rdx, r13
0061C88E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0061C892  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061C897  E8 D4 35 49 00                  call 0x140aafe70
0061C89C  89 45 F8                        mov dword ptr [rbp - 8], eax
0061C89F  4D 85 F6                        test r14, r14
0061C8A2  74 63                           je 0x14061c907
0061C8A4  40 32 FF                        xor dil, dil
0061C8A7  40 38 3D 0A 80 8E 00            cmp byte ptr [rip + 0x8e800a], dil
0061C8AE  75 0C                           jne 0x14061c8bc
0061C8B0  F7 05 C6 80 8E 00 00 08 00 00   test dword ptr [rip + 0x8e80c6], 0x800
0061C8BA  74 13                           je 0x14061c8cf
0061C8BC  48 8D 0D BD 75 8E 00            lea rcx, [rip + 0x8e75bd]
0061C8C3  E8 58 9D BF FF                  call 0x140216620
0061C8C8  40 8A F8                        mov dil, al
0061C8CB  84 C0                           test al, al
0061C8CD  74 38                           je 0x14061c907
0061C8CF  49 8D 76 30                     lea rsi, [r14 + 0x30]
0061C8D3  48 8B 1E                        mov rbx, qword ptr [rsi]
0061C8D6  EB 19                           jmp 0x14061c8f1
0061C8D8  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C8DC  48 85 C0                        test rax, rax
0061C8DF  74 0D                           je 0x14061c8ee
0061C8E1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C8E5  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0061C8E9  E8 E2 E1 09 00                  call 0x1406baad0
0061C8EE  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C8F1  48 3B DE                        cmp rbx, rsi
0061C8F4  75 E2                           jne 0x14061c8d8
0061C8F6  40 84 FF                        test dil, dil
0061C8F9  74 0C                           je 0x14061c907
0061C8FB  48 8D 0D 7E 75 8E 00            lea rcx, [rip + 0x8e757e]
0061C902  E8 79 D5 D2 FF                  call 0x140349e80
0061C907  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0061C90A  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0061C90F  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0061C913  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0061C917  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0061C91B  49 8B E3                        mov rsp, r11
0061C91E  41 5F                           pop r15
0061C920  41 5E                           pop r14
0061C922  41 5D                           pop r13
0061C924  41 5C                           pop r12
0061C926  5D                              pop rbp
0061C927  C3                              ret
0061C928  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifCmRegisterCallbackExWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    result = DifGetAPIThunkContextById(429, a2, a2 + 64, a4);
    if (result == 0) goto loc_0061C878;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061C7E3;
    v_stack_m68 = v_stack_p0;
    goto loc_0061C7F1;
loc_0061C7E3:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a2 + 64, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = a5;
    v_stack_m60 = a6;
    v_stack_m40 = 0;
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9339065)) != 0) goto loc_0061C82D;
    if (((*(unsigned int *)(v_rip + 9339221)) & (0x800ULL)) == 0) goto loc_0061C840;
loc_0061C82D:
    result = ExAcquireRundownProtection(v_rip + 9336396, a2, a2 + 64, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C878;
loc_0061C840:
    goto loc_0061C862;
loc_0061C849:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a2 + 64, a4);
    }
loc_0061C862:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061C849;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9336333;
        result = ExReleaseRundownProtection(a1, a2, a2 + 64, a4);
    }
    v_stack_m70 = a6;
    v_stack_m78 = a5;
    result = CmRegisterCallbackEx(v_stack_p8, 0, a3, a4);
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0061C907;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9338890)) != 0) goto loc_0061C8BC;
    if (((*(unsigned int *)(v_rip + 9339078)) & (0x800ULL)) == 0) goto loc_0061C8CF;
loc_0061C8BC:
    result = ExAcquireRundownProtection(v_rip + 9336253, 0, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C907;
loc_0061C8CF:
    goto loc_0061C8F1;
loc_0061C8D8:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, 0, a3, a4);
    }
loc_0061C8F1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0061C8D8;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9336190;
        result = ExReleaseRundownProtection(a1, 0, a3, a4);
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifCmRegisterCallbackExWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, Arg4);
    result = DifGetAPIThunkContextById(429, Arg2, Arg2 + 64, Arg4);
    if (result == 0) goto loc_0061C878;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061C7E3;
    v_stack_m68 = v_stack_p0;
    goto loc_0061C7F1;
loc_0061C7E3:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg2 + 64, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m58 = Arg5;
    v_stack_m60 = Arg6;
    v_stack_m40 = 0;
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8E80B9)) != 0) goto loc_0061C82D;
    if (((*(uint32_t *)(v_rip + 0x8E8155)) & (0x800ULL)) == 0) goto loc_0061C840;
loc_0061C82D:
    result = ExAcquireRundownProtection(v_rip + 9336396, Arg2, Arg2 + 64, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C878;
loc_0061C840:
    goto loc_0061C862;
loc_0061C849:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg2 + 64, Arg4);
    }
loc_0061C862:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061C849;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9336333;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg2 + 64, Arg4);
    }
    v_stack_m70 = Arg6;
    v_stack_m78 = Arg5;
    result = CmRegisterCallbackEx(v_stack_p8, 0, Arg3, Arg4);
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0061C907;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E800A)) != 0) goto loc_0061C8BC;
    if (((*(uint32_t *)(v_rip + 0x8E80C6)) & (0x800ULL)) == 0) goto loc_0061C8CF;
loc_0061C8BC:
    result = ExAcquireRundownProtection(v_rip + 9336253, 0, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C907;
loc_0061C8CF:
    goto loc_0061C8F1;
loc_0061C8D8:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, 0, Arg3, Arg4);
    }
loc_0061C8F1:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0061C8D8;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9336190;
        result = ExReleaseRundownProtection(Arg1, 0, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061C780&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061C780[BB_0061C780]
  bb_0061C7D1[BB_0061C7D1]
  bb_0061C7D9[BB_0061C7D9]
  bb_0061C7E3[BB_0061C7E3]
  bb_0061C7E8[BB_0061C7E8]
  bb_0061C7F1[BB_0061C7F1]
  bb_0061C821[BB_0061C821]
  bb_0061C82D[BB_0061C82D]
  bb_0061C840[BB_0061C840]
  bb_0061C849[BB_0061C849]
  bb_0061C852[BB_0061C852]
  bb_0061C85F[BB_0061C85F]
  bb_0061C862[BB_0061C862]
  bb_0061C867[BB_0061C867]
  bb_0061C86C[BB_0061C86C]
  bb_0061C878[BB_0061C878]
  bb_0061C8A4[BB_0061C8A4]
  bb_0061C8B0[BB_0061C8B0]
  bb_0061C8BC[BB_0061C8BC]
  bb_0061C8CF[BB_0061C8CF]
  bb_0061C8D8[BB_0061C8D8]
  bb_0061C8E1[BB_0061C8E1]
  bb_0061C8EE[BB_0061C8EE]
  bb_0061C8F1[BB_0061C8F1]
  bb_0061C8F6[BB_0061C8F6]
  bb_0061C8FB[BB_0061C8FB]
  bb_0061C907[BB_0061C907]
  bb_0061C928[BB_0061C928]
  bb_0061C780 -->|branch| bb_0061C878
  bb_0061C780 -->|fallthrough| bb_0061C7D1
  bb_0061C7D1 -->|branch| bb_0061C7E3
  bb_0061C7D1 -->|fallthrough| bb_0061C7D9
  bb_0061C7D9 -->|branch| bb_0061C7F1
  bb_0061C7E3 -->|branch| bb_0061C7F1
  bb_0061C7E3 -->|fallthrough| bb_0061C7E8
  bb_0061C7E8 -->|flow| bb_0061C7F1
  bb_0061C7F1 -->|branch| bb_0061C82D
  bb_0061C7F1 -->|fallthrough| bb_0061C821
  bb_0061C821 -->|branch| bb_0061C840
  bb_0061C821 -->|fallthrough| bb_0061C82D
  bb_0061C82D -->|branch| bb_0061C878
  bb_0061C82D -->|fallthrough| bb_0061C840
  bb_0061C840 -->|branch| bb_0061C862
  bb_0061C849 -->|branch| bb_0061C85F
  bb_0061C849 -->|fallthrough| bb_0061C852
  bb_0061C852 -->|flow| bb_0061C85F
  bb_0061C85F -->|flow| bb_0061C862
  bb_0061C862 -->|branch| bb_0061C849
  bb_0061C862 -->|fallthrough| bb_0061C867
  bb_0061C867 -->|branch| bb_0061C878
  bb_0061C867 -->|fallthrough| bb_0061C86C
  bb_0061C86C -->|flow| bb_0061C878
  bb_0061C878 -->|branch| bb_0061C907
  bb_0061C878 -->|fallthrough| bb_0061C8A4
  bb_0061C8A4 -->|branch| bb_0061C8BC
  bb_0061C8A4 -->|fallthrough| bb_0061C8B0
  bb_0061C8B0 -->|branch| bb_0061C8CF
  bb_0061C8B0 -->|fallthrough| bb_0061C8BC
  bb_0061C8BC -->|branch| bb_0061C907
  bb_0061C8BC -->|fallthrough| bb_0061C8CF
  bb_0061C8CF -->|branch| bb_0061C8F1
  bb_0061C8D8 -->|branch| bb_0061C8EE
  bb_0061C8D8 -->|fallthrough| bb_0061C8E1
  bb_0061C8E1 -->|flow| bb_0061C8EE
  bb_0061C8EE -->|flow| bb_0061C8F1
  bb_0061C8F1 -->|branch| bb_0061C8D8
  bb_0061C8F1 -->|fallthrough| bb_0061C8F6
  bb_0061C8F6 -->|branch| bb_0061C907
  bb_0061C8F6 -->|fallthrough| bb_0061C8FB
  bb_0061C8FB -->|flow| bb_0061C907
```
