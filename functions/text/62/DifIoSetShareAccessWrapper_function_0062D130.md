# DifIoSetShareAccessWrapper

- RVA: `0x0062D130`–`0x0062D2AB` (길이 `379` bytes)
- VA: `0x000000014062D130`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC264`
- 디코드: `107`개 명령, `379/379` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062D168` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062D190` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062D1CD` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D1F4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D20D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062D21E` → [IoSetShareAccess](../../page/9A/IoSetShareAccess_function_009A3FF0.md) (function, `0x009A3FF0`)
- `0x0062D247` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062D26E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062D287` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062D1A2` → RVA `0x00F048B8` (`.data`; read)
- `0x0062D1BA` → RVA `0x00F04980` (`.data`; read)
- `0x0062D1C6` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062D21E` → [IoSetShareAccess](../../page/9A/IoSetShareAccess_function_009A3FF0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062D130  48 8B C4                        mov rax, rsp
0062D133  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062D137  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062D13B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062D13F  57                              push rdi
0062D140  41 54                           push r12
0062D142  41 55                           push r13
0062D144  41 56                           push r14
0062D146  41 57                           push r15
0062D148  48 83 EC 40                     sub rsp, 0x40
0062D14C  0F 57 C0                        xorps xmm0, xmm0
0062D14F  44 8B E9                        mov r13d, ecx
0062D152  B9 36 01 00 00                  mov ecx, 0x136
0062D157  4D 8B F1                        mov r14, r9
0062D15A  0F 11 40 B8                     movups xmmword ptr [rax - 0x48], xmm0
0062D15E  4D 8B F8                        mov r15, r8
0062D161  44 8B E2                        mov r12d, edx
0062D164  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062D168  E8 C7 88 E6 FF                  call 0x140495a34
0062D16D  48 8B F0                        mov rsi, rax
0062D170  48 85 C0                        test rax, rax
0062D173  0F 84 99 00 00 00               je 0x14062d212
0062D179  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062D17C  A8 18                           test al, 0x18
0062D17E  74 0C                           je 0x14062d18c
0062D180  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0062D185  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062D18A  EB 0E                           jmp 0x14062d19a
0062D18C  A8 04                           test al, 4
0062D18E  74 0A                           je 0x14062d19a
0062D190  E8 73 6A EA FF                  call 0x1404d3c08
0062D195  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062D19A  40 32 ED                        xor bpl, bpl
0062D19D  44 89 6C 24 3C                  mov dword ptr [rsp + 0x3c], r13d
0062D1A2  40 38 2D 0F 77 8D 00            cmp byte ptr [rip + 0x8d770f], bpl
0062D1A9  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0062D1AE  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062D1B3  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0062D1B8  75 0C                           jne 0x14062d1c6
0062D1BA  F7 05 BC 77 8D 00 00 08 00 00   test dword ptr [rip + 0x8d77bc], 0x800
0062D1C4  74 13                           je 0x14062d1d9
0062D1C6  48 8D 0D B3 6C 8D 00            lea rcx, [rip + 0x8d6cb3]
0062D1CD  E8 4E 94 BE FF                  call 0x140216620
0062D1D2  40 8A E8                        mov bpl, al
0062D1D5  84 C0                           test al, al
0062D1D7  74 39                           je 0x14062d212
0062D1D9  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062D1DD  48 8B 1F                        mov rbx, qword ptr [rdi]
0062D1E0  EB 1A                           jmp 0x14062d1fc
0062D1E2  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D1E6  48 85 C0                        test rax, rax
0062D1E9  74 0E                           je 0x14062d1f9
0062D1EB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D1EF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062D1F4  E8 D7 D8 08 00                  call 0x1406baad0
0062D1F9  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D1FC  48 3B DF                        cmp rbx, rdi
0062D1FF  75 E1                           jne 0x14062d1e2
0062D201  40 84 ED                        test bpl, bpl
0062D204  74 0C                           je 0x14062d212
0062D206  48 8D 0D 73 6C 8D 00            lea rcx, [rip + 0x8d6c73]
0062D20D  E8 6E CC D1 FF                  call 0x140349e80
0062D212  4D 8B CE                        mov r9, r14
0062D215  4D 8B C7                        mov r8, r15
0062D218  41 8B D4                        mov edx, r12d
0062D21B  41 8B CD                        mov ecx, r13d
0062D21E  E8 CD 6D 37 00                  call 0x1409a3ff0
0062D223  48 85 F6                        test rsi, rsi
0062D226  74 64                           je 0x14062d28c
0062D228  40 32 FF                        xor dil, dil
0062D22B  40 38 3D 86 76 8D 00            cmp byte ptr [rip + 0x8d7686], dil
0062D232  75 0C                           jne 0x14062d240
0062D234  F7 05 42 77 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7742], 0x800
0062D23E  74 13                           je 0x14062d253
0062D240  48 8D 0D 39 6C 8D 00            lea rcx, [rip + 0x8d6c39]
0062D247  E8 D4 93 BE FF                  call 0x140216620
0062D24C  40 8A F8                        mov dil, al
0062D24F  84 C0                           test al, al
0062D251  74 39                           je 0x14062d28c
0062D253  48 83 C6 30                     add rsi, 0x30
0062D257  48 8B 1E                        mov rbx, qword ptr [rsi]
0062D25A  EB 1A                           jmp 0x14062d276
0062D25C  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062D260  48 85 C0                        test rax, rax
0062D263  74 0E                           je 0x14062d273
0062D265  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062D269  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062D26E  E8 5D D8 08 00                  call 0x1406baad0
0062D273  48 8B 1B                        mov rbx, qword ptr [rbx]
0062D276  48 3B DE                        cmp rbx, rsi
0062D279  75 E1                           jne 0x14062d25c
0062D27B  40 84 FF                        test dil, dil
0062D27E  74 0C                           je 0x14062d28c
0062D280  48 8D 0D F9 6B 8D 00            lea rcx, [rip + 0x8d6bf9]
0062D287  E8 F4 CB D1 FF                  call 0x140349e80
0062D28C  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
0062D291  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0062D295  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
0062D299  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0062D29D  49 8B E3                        mov rsp, r11
0062D2A0  41 5F                           pop r15
0062D2A2  41 5E                           pop r14
0062D2A4  41 5D                           pop r13
0062D2A6  41 5C                           pop r12
0062D2A8  5F                              pop rdi
0062D2A9  C3                              ret
0062D2AA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoSetShareAccessWrapper(int a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p0;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    result = DifGetAPIThunkContextById(310, a2, a3, a4);
    if (result == 0) goto loc_0062D212;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062D18C;
    v_stack_m48 = v_stack_p0;
    goto loc_0062D19A;
loc_0062D18C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m48 = result;
    }
    v_rbp = 0;
    v_stack_m2C = (unsigned int)((unsigned int)(a1));
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    v_stack_m38 = a3;
    v_stack_m40 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9271055)) != 0) goto loc_0062D1C6;
    if (((*(unsigned int *)(v_rip + 9271228)) & (0x800ULL)) == 0) goto loc_0062D1D9;
loc_0062D1C6:
    result = ExAcquireRundownProtection(v_rip + 9268403, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D212;
loc_0062D1D9:
    goto loc_0062D1FC;
loc_0062D1E2:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062D1FC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062D1E2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9268339;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoSetShareAccess((unsigned int)((unsigned int)((unsigned int)(a1))), (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_0062D28C;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9270918)) != 0) goto loc_0062D240;
    if (((*(unsigned int *)(v_rip + 9271106)) & (0x800ULL)) == 0) goto loc_0062D253;
loc_0062D240:
    result = ExAcquireRundownProtection(v_rip + 9268281, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062D28C;
loc_0062D253:
    v_rsi = (result) + (48);
    goto loc_0062D276;
loc_0062D25C:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m48;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0062D276:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062D25C;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9268217;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoSetShareAccessWrapper(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p0;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    result = DifGetAPIThunkContextById(310, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062D212;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062D18C;
    v_stack_m48 = v_stack_p0;
    goto loc_0062D19A;
loc_0062D18C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m48 = result;
    }
    local_rbp = 0;
    v_stack_m2C = (uint32_t)((uint32_t)(Arg1));
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m38 = Arg3;
    v_stack_m40 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8D770F)) != 0) goto loc_0062D1C6;
    if (((*(uint32_t *)(v_rip + 0x8D77BC)) & (0x800ULL)) == 0) goto loc_0062D1D9;
loc_0062D1C6:
    result = ExAcquireRundownProtection(v_rip + 9268403, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062D212;
loc_0062D1D9:
    goto loc_0062D1FC;
loc_0062D1E2:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062D1FC:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062D1E2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9268339;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = IoSetShareAccess((uint32_t)((uint32_t)((uint32_t)(Arg1))), (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if (result == 0) goto loc_0062D28C;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D7686)) != 0) goto loc_0062D240;
    if (((*(uint32_t *)(v_rip + 0x8D7742)) & (0x800ULL)) == 0) goto loc_0062D253;
loc_0062D240:
    result = ExAcquireRundownProtection(v_rip + 9268281, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062D28C;
loc_0062D253:
    local_rsi = (result) + (48);
    goto loc_0062D276;
loc_0062D25C:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m48;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
loc_0062D276:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062D25C;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9268217;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062D130&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062D130[BB_0062D130]
  bb_0062D179[BB_0062D179]
  bb_0062D180[BB_0062D180]
  bb_0062D18C[BB_0062D18C]
  bb_0062D190[BB_0062D190]
  bb_0062D19A[BB_0062D19A]
  bb_0062D1BA[BB_0062D1BA]
  bb_0062D1C6[BB_0062D1C6]
  bb_0062D1D9[BB_0062D1D9]
  bb_0062D1E2[BB_0062D1E2]
  bb_0062D1EB[BB_0062D1EB]
  bb_0062D1F9[BB_0062D1F9]
  bb_0062D1FC[BB_0062D1FC]
  bb_0062D201[BB_0062D201]
  bb_0062D206[BB_0062D206]
  bb_0062D212[BB_0062D212]
  bb_0062D228[BB_0062D228]
  bb_0062D234[BB_0062D234]
  bb_0062D240[BB_0062D240]
  bb_0062D253[BB_0062D253]
  bb_0062D25C[BB_0062D25C]
  bb_0062D265[BB_0062D265]
  bb_0062D273[BB_0062D273]
  bb_0062D276[BB_0062D276]
  bb_0062D27B[BB_0062D27B]
  bb_0062D280[BB_0062D280]
  bb_0062D28C[BB_0062D28C]
  bb_0062D2AA[BB_0062D2AA]
  bb_0062D130 -->|branch| bb_0062D212
  bb_0062D130 -->|fallthrough| bb_0062D179
  bb_0062D179 -->|branch| bb_0062D18C
  bb_0062D179 -->|fallthrough| bb_0062D180
  bb_0062D180 -->|branch| bb_0062D19A
  bb_0062D18C -->|branch| bb_0062D19A
  bb_0062D18C -->|fallthrough| bb_0062D190
  bb_0062D190 -->|flow| bb_0062D19A
  bb_0062D19A -->|branch| bb_0062D1C6
  bb_0062D19A -->|fallthrough| bb_0062D1BA
  bb_0062D1BA -->|branch| bb_0062D1D9
  bb_0062D1BA -->|fallthrough| bb_0062D1C6
  bb_0062D1C6 -->|branch| bb_0062D212
  bb_0062D1C6 -->|fallthrough| bb_0062D1D9
  bb_0062D1D9 -->|branch| bb_0062D1FC
  bb_0062D1E2 -->|branch| bb_0062D1F9
  bb_0062D1E2 -->|fallthrough| bb_0062D1EB
  bb_0062D1EB -->|flow| bb_0062D1F9
  bb_0062D1F9 -->|flow| bb_0062D1FC
  bb_0062D1FC -->|branch| bb_0062D1E2
  bb_0062D1FC -->|fallthrough| bb_0062D201
  bb_0062D201 -->|branch| bb_0062D212
  bb_0062D201 -->|fallthrough| bb_0062D206
  bb_0062D206 -->|flow| bb_0062D212
  bb_0062D212 -->|branch| bb_0062D28C
  bb_0062D212 -->|fallthrough| bb_0062D228
  bb_0062D228 -->|branch| bb_0062D240
  bb_0062D228 -->|fallthrough| bb_0062D234
  bb_0062D234 -->|branch| bb_0062D253
  bb_0062D234 -->|fallthrough| bb_0062D240
  bb_0062D240 -->|branch| bb_0062D28C
  bb_0062D240 -->|fallthrough| bb_0062D253
  bb_0062D253 -->|branch| bb_0062D276
  bb_0062D25C -->|branch| bb_0062D273
  bb_0062D25C -->|fallthrough| bb_0062D265
  bb_0062D265 -->|flow| bb_0062D273
  bb_0062D273 -->|flow| bb_0062D276
  bb_0062D276 -->|branch| bb_0062D25C
  bb_0062D276 -->|fallthrough| bb_0062D27B
  bb_0062D27B -->|branch| bb_0062D28C
  bb_0062D27B -->|fallthrough| bb_0062D280
  bb_0062D280 -->|flow| bb_0062D28C
```
