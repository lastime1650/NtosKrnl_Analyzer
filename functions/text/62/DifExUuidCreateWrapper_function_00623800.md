# DifExUuidCreateWrapper

- RVA: `0x00623800`–`0x0062395F` (길이 `351` bytes)
- VA: `0x0000000140623800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062382F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00623857` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00623885` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006238AC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006238C5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006238CD` → [ExUuidCreate](../../page/91/ExUuidCreate_function_00917500.md) (function, `0x00917500`)
- `0x006238FA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623921` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062393A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00623869` → RVA `0x00F048B8` (`.data`; read)
- `0x00623872` → RVA `0x00F04980` (`.data`; read)
- `0x0062387E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006238CD` → [ExUuidCreate](../../page/91/ExUuidCreate_function_00917500.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00623800  4C 8B DC                        mov r11, rsp
00623803  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00623807  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062380B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062380F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00623813  41 56                           push r14
00623815  48 83 EC 40                     sub rsp, 0x40
00623819  33 C0                           xor eax, eax
0062381B  0F 57 C0                        xorps xmm0, xmm0
0062381E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00623823  48 8B E9                        mov rbp, rcx
00623826  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062382A  B9 7D 01 00 00                  mov ecx, 0x17d
0062382F  E8 00 22 E7 FF                  call 0x140495a34
00623834  48 8B F0                        mov rsi, rax
00623837  48 85 C0                        test rax, rax
0062383A  0F 84 8A 00 00 00               je 0x1406238ca
00623840  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00623843  A8 18                           test al, 0x18
00623845  74 0C                           je 0x140623853
00623847  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062384C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00623851  EB 0E                           jmp 0x140623861
00623853  A8 04                           test al, 4
00623855  74 0A                           je 0x140623861
00623857  E8 AC 03 EB FF                  call 0x1404d3c08
0062385C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00623861  40 32 FF                        xor dil, dil
00623864  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00623869  40 38 3D 48 10 8E 00            cmp byte ptr [rip + 0x8e1048], dil
00623870  75 0C                           jne 0x14062387e
00623872  F7 05 04 11 8E 00 00 08 00 00   test dword ptr [rip + 0x8e1104], 0x800
0062387C  74 13                           je 0x140623891
0062387E  48 8D 0D FB 05 8E 00            lea rcx, [rip + 0x8e05fb]
00623885  E8 96 2D BF FF                  call 0x140216620
0062388A  40 8A F8                        mov dil, al
0062388D  84 C0                           test al, al
0062388F  74 39                           je 0x1406238ca
00623891  4C 8D 76 20                     lea r14, [rsi + 0x20]
00623895  49 8B 1E                        mov rbx, qword ptr [r14]
00623898  EB 1A                           jmp 0x1406238b4
0062389A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062389E  48 85 C0                        test rax, rax
006238A1  74 0E                           je 0x1406238b1
006238A3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006238A7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006238AC  E8 1F 72 09 00                  call 0x1406baad0
006238B1  48 8B 1B                        mov rbx, qword ptr [rbx]
006238B4  49 3B DE                        cmp rbx, r14
006238B7  75 E1                           jne 0x14062389a
006238B9  40 84 FF                        test dil, dil
006238BC  74 0C                           je 0x1406238ca
006238BE  48 8D 0D BB 05 8E 00            lea rcx, [rip + 0x8e05bb]
006238C5  E8 B6 65 D2 FF                  call 0x140349e80
006238CA  48 8B CD                        mov rcx, rbp
006238CD  E8 2E 3C 2F 00                  call 0x140917500
006238D2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006238D6  48 85 F6                        test rsi, rsi
006238D9  74 64                           je 0x14062393f
006238DB  40 32 FF                        xor dil, dil
006238DE  40 38 3D D3 0F 8E 00            cmp byte ptr [rip + 0x8e0fd3], dil
006238E5  75 0C                           jne 0x1406238f3
006238E7  F7 05 8F 10 8E 00 00 08 00 00   test dword ptr [rip + 0x8e108f], 0x800
006238F1  74 13                           je 0x140623906
006238F3  48 8D 0D 86 05 8E 00            lea rcx, [rip + 0x8e0586]
006238FA  E8 21 2D BF FF                  call 0x140216620
006238FF  40 8A F8                        mov dil, al
00623902  84 C0                           test al, al
00623904  74 39                           je 0x14062393f
00623906  48 83 C6 30                     add rsi, 0x30
0062390A  48 8B 1E                        mov rbx, qword ptr [rsi]
0062390D  EB 1A                           jmp 0x140623929
0062390F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623913  48 85 C0                        test rax, rax
00623916  74 0E                           je 0x140623926
00623918  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062391C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623921  E8 AA 71 09 00                  call 0x1406baad0
00623926  48 8B 1B                        mov rbx, qword ptr [rbx]
00623929  48 3B DE                        cmp rbx, rsi
0062392C  75 E1                           jne 0x14062390f
0062392E  40 84 FF                        test dil, dil
00623931  74 0C                           je 0x14062393f
00623933  48 8D 0D 46 05 8E 00            lea rcx, [rip + 0x8e0546]
0062393A  E8 41 65 D2 FF                  call 0x140349e80
0062393F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00623943  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00623948  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062394D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00623952  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00623957  48 83 C4 40                     add rsp, 0x40
0062395B  41 5E                           pop r14
0062395D  C3                              ret
0062395E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExUuidCreateWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(381, a2, a3, a4);
    if (result == 0) goto loc_006238CA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00623853;
    v_stack_m28 = v_stack_p0;
    goto loc_00623861;
loc_00623853:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9310280)) != 0) goto loc_0062387E;
    if (((*(unsigned int *)(v_rip + 9310468)) & (0x800ULL)) == 0) goto loc_00623891;
loc_0062387E:
    result = ExAcquireRundownProtection(v_rip + 9307643, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006238CA;
loc_00623891:
    goto loc_006238B4;
loc_0062389A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006238B4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062389A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9307579;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExUuidCreate(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0062393F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9310163)) != 0) goto loc_006238F3;
    if (((*(unsigned int *)(v_rip + 9310351)) & (0x800ULL)) == 0) goto loc_00623906;
loc_006238F3:
    result = ExAcquireRundownProtection(v_rip + 9307526, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062393F;
loc_00623906:
    v_rsi = (result) + (48);
    goto loc_00623929;
loc_0062390F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00623929:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062390F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9307462;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifExUuidCreateWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(381, a2, a3, a4);
    if (result == 0) goto loc_006238CA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00623853;
    v_stack_m28 = v_stack_p0;
    goto loc_00623861;
loc_00623853:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E1048)) != 0) goto loc_0062387E;
    if (((*(uint32_t *)(v_rip + 0x8E1104)) & (0x800ULL)) == 0) goto loc_00623891;
loc_0062387E:
    result = ExAcquireRundownProtection(v_rip + 9307643, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006238CA;
loc_00623891:
    goto loc_006238B4;
loc_0062389A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006238B4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062389A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9307579;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExUuidCreate(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0062393F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E0FD3)) != 0) goto loc_006238F3;
    if (((*(uint32_t *)(v_rip + 0x8E108F)) & (0x800ULL)) == 0) goto loc_00623906;
loc_006238F3:
    result = ExAcquireRundownProtection(v_rip + 9307526, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062393F;
loc_00623906:
    local_rsi = (result) + (48);
    goto loc_00623929;
loc_0062390F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00623929:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062390F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9307462;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00623800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00623800[BB_00623800]
  bb_00623840[BB_00623840]
  bb_00623847[BB_00623847]
  bb_00623853[BB_00623853]
  bb_00623857[BB_00623857]
  bb_00623861[BB_00623861]
  bb_00623872[BB_00623872]
  bb_0062387E[BB_0062387E]
  bb_00623891[BB_00623891]
  bb_0062389A[BB_0062389A]
  bb_006238A3[BB_006238A3]
  bb_006238B1[BB_006238B1]
  bb_006238B4[BB_006238B4]
  bb_006238B9[BB_006238B9]
  bb_006238BE[BB_006238BE]
  bb_006238CA[BB_006238CA]
  bb_006238DB[BB_006238DB]
  bb_006238E7[BB_006238E7]
  bb_006238F3[BB_006238F3]
  bb_00623906[BB_00623906]
  bb_0062390F[BB_0062390F]
  bb_00623918[BB_00623918]
  bb_00623926[BB_00623926]
  bb_00623929[BB_00623929]
  bb_0062392E[BB_0062392E]
  bb_00623933[BB_00623933]
  bb_0062393F[BB_0062393F]
  bb_0062395E[BB_0062395E]
  bb_00623800 -->|branch| bb_006238CA
  bb_00623800 -->|fallthrough| bb_00623840
  bb_00623840 -->|branch| bb_00623853
  bb_00623840 -->|fallthrough| bb_00623847
  bb_00623847 -->|branch| bb_00623861
  bb_00623853 -->|branch| bb_00623861
  bb_00623853 -->|fallthrough| bb_00623857
  bb_00623857 -->|flow| bb_00623861
  bb_00623861 -->|branch| bb_0062387E
  bb_00623861 -->|fallthrough| bb_00623872
  bb_00623872 -->|branch| bb_00623891
  bb_00623872 -->|fallthrough| bb_0062387E
  bb_0062387E -->|branch| bb_006238CA
  bb_0062387E -->|fallthrough| bb_00623891
  bb_00623891 -->|branch| bb_006238B4
  bb_0062389A -->|branch| bb_006238B1
  bb_0062389A -->|fallthrough| bb_006238A3
  bb_006238A3 -->|flow| bb_006238B1
  bb_006238B1 -->|flow| bb_006238B4
  bb_006238B4 -->|branch| bb_0062389A
  bb_006238B4 -->|fallthrough| bb_006238B9
  bb_006238B9 -->|branch| bb_006238CA
  bb_006238B9 -->|fallthrough| bb_006238BE
  bb_006238BE -->|flow| bb_006238CA
  bb_006238CA -->|branch| bb_0062393F
  bb_006238CA -->|fallthrough| bb_006238DB
  bb_006238DB -->|branch| bb_006238F3
  bb_006238DB -->|fallthrough| bb_006238E7
  bb_006238E7 -->|branch| bb_00623906
  bb_006238E7 -->|fallthrough| bb_006238F3
  bb_006238F3 -->|branch| bb_0062393F
  bb_006238F3 -->|fallthrough| bb_00623906
  bb_00623906 -->|branch| bb_00623929
  bb_0062390F -->|branch| bb_00623926
  bb_0062390F -->|fallthrough| bb_00623918
  bb_00623918 -->|flow| bb_00623926
  bb_00623926 -->|flow| bb_00623929
  bb_00623929 -->|branch| bb_0062390F
  bb_00623929 -->|fallthrough| bb_0062392E
  bb_0062392E -->|branch| bb_0062393F
  bb_0062392E -->|fallthrough| bb_00623933
  bb_00623933 -->|flow| bb_0062393F
```
