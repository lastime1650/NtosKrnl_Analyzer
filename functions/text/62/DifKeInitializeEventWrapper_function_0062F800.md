# DifKeInitializeEventWrapper

- RVA: `0x0062F800`–`0x0062F980` (길이 `384` bytes)
- VA: `0x000000014062F800`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `104`개 명령, `384/384` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062F83A` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062F862` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062F89A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F8C1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F8DA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062F91B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062F942` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062F95B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062F874` → RVA `0x00F048B8` (`.data`; read)
- `0x0062F887` → RVA `0x00F04980` (`.data`; read)
- `0x0062F893` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062F800  4C 8B DC                        mov r11, rsp
0062F803  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062F807  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062F80B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062F80F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062F813  41 54                           push r12
0062F815  41 56                           push r14
0062F817  41 57                           push r15
0062F819  48 83 EC 40                     sub rsp, 0x40
0062F81D  33 C0                           xor eax, eax
0062F81F  45 0F B6 F8                     movzx r15d, r8b
0062F823  0F 57 C0                        xorps xmm0, xmm0
0062F826  48 8B F9                        mov rdi, rcx
0062F829  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062F82E  B9 1B 01 00 00                  mov ecx, 0x11b
0062F833  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0062F837  44 8B E2                        mov r12d, edx
0062F83A  E8 F5 61 E6 FF                  call 0x140495a34
0062F83F  48 8B F0                        mov rsi, rax
0062F842  48 85 C0                        test rax, rax
0062F845  0F 84 94 00 00 00               je 0x14062f8df
0062F84B  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062F84E  A8 18                           test al, 0x18
0062F850  74 0C                           je 0x14062f85e
0062F852  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062F857  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062F85C  EB 0E                           jmp 0x14062f86c
0062F85E  A8 04                           test al, 4
0062F860  74 0A                           je 0x14062f86c
0062F862  E8 A1 43 EA FF                  call 0x1404d3c08
0062F867  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062F86C  40 32 ED                        xor bpl, bpl
0062F86F  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0062F874  40 38 2D 3D 50 8D 00            cmp byte ptr [rip + 0x8d503d], bpl
0062F87B  44 89 64 24 2C                  mov dword ptr [rsp + 0x2c], r12d
0062F880  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
0062F885  75 0C                           jne 0x14062f893
0062F887  F7 05 EF 50 8D 00 00 08 00 00   test dword ptr [rip + 0x8d50ef], 0x800
0062F891  74 13                           je 0x14062f8a6
0062F893  48 8D 0D E6 45 8D 00            lea rcx, [rip + 0x8d45e6]
0062F89A  E8 81 6D BE FF                  call 0x140216620
0062F89F  40 8A E8                        mov bpl, al
0062F8A2  84 C0                           test al, al
0062F8A4  74 39                           je 0x14062f8df
0062F8A6  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062F8AA  49 8B 1E                        mov rbx, qword ptr [r14]
0062F8AD  EB 1A                           jmp 0x14062f8c9
0062F8AF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F8B3  48 85 C0                        test rax, rax
0062F8B6  74 0E                           je 0x14062f8c6
0062F8B8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F8BC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062F8C1  E8 0A B2 08 00                  call 0x1406baad0
0062F8C6  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F8C9  49 3B DE                        cmp rbx, r14
0062F8CC  75 E1                           jne 0x14062f8af
0062F8CE  40 84 ED                        test bpl, bpl
0062F8D1  74 0C                           je 0x14062f8df
0062F8D3  48 8D 0D A6 45 8D 00            lea rcx, [rip + 0x8d45a6]
0062F8DA  E8 A1 A5 D1 FF                  call 0x140349e80
0062F8DF  44 88 27                        mov byte ptr [rdi], r12b
0062F8E2  48 8D 47 08                     lea rax, [rdi + 8]
0062F8E6  66 C7 47 01 00 06               mov word ptr [rdi + 1], 0x600
0062F8EC  44 89 7F 04                     mov dword ptr [rdi + 4], r15d
0062F8F0  48 89 40 08                     mov qword ptr [rax + 8], rax
0062F8F4  48 89 00                        mov qword ptr [rax], rax
0062F8F7  48 85 F6                        test rsi, rsi
0062F8FA  74 64                           je 0x14062f960
0062F8FC  40 32 FF                        xor dil, dil
0062F8FF  40 38 3D B2 4F 8D 00            cmp byte ptr [rip + 0x8d4fb2], dil
0062F906  75 0C                           jne 0x14062f914
0062F908  F7 05 6E 50 8D 00 00 08 00 00   test dword ptr [rip + 0x8d506e], 0x800
0062F912  74 13                           je 0x14062f927
0062F914  48 8D 0D 65 45 8D 00            lea rcx, [rip + 0x8d4565]
0062F91B  E8 00 6D BE FF                  call 0x140216620
0062F920  40 8A F8                        mov dil, al
0062F923  84 C0                           test al, al
0062F925  74 39                           je 0x14062f960
0062F927  48 83 C6 30                     add rsi, 0x30
0062F92B  48 8B 1E                        mov rbx, qword ptr [rsi]
0062F92E  EB 1A                           jmp 0x14062f94a
0062F930  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062F934  48 85 C0                        test rax, rax
0062F937  74 0E                           je 0x14062f947
0062F939  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062F93D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062F942  E8 89 B1 08 00                  call 0x1406baad0
0062F947  48 8B 1B                        mov rbx, qword ptr [rbx]
0062F94A  48 3B DE                        cmp rbx, rsi
0062F94D  75 E1                           jne 0x14062f930
0062F94F  40 84 FF                        test dil, dil
0062F952  74 0C                           je 0x14062f960
0062F954  48 8D 0D 25 45 8D 00            lea rcx, [rip + 0x8d4525]
0062F95B  E8 20 A5 D1 FF                  call 0x140349e80
0062F960  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062F965  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062F96A  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062F96F  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062F974  48 83 C4 40                     add rsp, 0x40
0062F978  41 5F                           pop r15
0062F97A  41 5E                           pop r14
0062F97C  41 5C                           pop r12
0062F97E  C3                              ret
0062F97F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInitializeEventWrapper(__int64 a1, int a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(283, a2, a3, a4);
    if (result == 0) goto loc_0062F8DF;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062F85E;
    v_stack_m38 = v_stack_p0;
    goto loc_0062F86C;
loc_0062F85E:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m2C = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9261117)) != 0) goto loc_0062F893;
    if (((*(unsigned int *)(v_rip + 9261295)) & (0x800ULL)) == 0) goto loc_0062F8A6;
loc_0062F893:
    result = ExAcquireRundownProtection(v_rip + 9258470, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F8DF;
loc_0062F8A6:
    goto loc_0062F8C9;
loc_0062F8AF:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F8C9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062F8AF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9258406;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(a1) = (unsigned __int8)((unsigned int)(a2));
    *(unsigned __int16 *)(a1 + 1) = 0x600ULL;
    *(unsigned int *)(a1 + 4) = a3;
    *(unsigned __int64 *)(a1 + 8 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 8) = a1 + 8;
    if (result == 0) goto loc_0062F960;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9260978)) != 0) goto loc_0062F914;
    if (((*(unsigned int *)(v_rip + 9261166)) & (0x800ULL)) == 0) goto loc_0062F927;
loc_0062F914:
    result = ExAcquireRundownProtection(v_rip + 9258341, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062F960;
loc_0062F927:
    v_rsi = (result) + (48);
    goto loc_0062F94A;
loc_0062F930:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062F94A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062F930;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9258277;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInitializeEventWrapper(void *Arg1, int32_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
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
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(283, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062F8DF;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062F85E;
    v_stack_m38 = v_stack_p0;
    goto loc_0062F86C;
loc_0062F85E:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m2C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D503D)) != 0) goto loc_0062F893;
    if (((*(uint32_t *)(v_rip + 0x8D50EF)) & (0x800ULL)) == 0) goto loc_0062F8A6;
loc_0062F893:
    result = ExAcquireRundownProtection(v_rip + 9258470, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F8DF;
loc_0062F8A6:
    goto loc_0062F8C9;
loc_0062F8AF:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062F8C9:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062F8AF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9258406;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    *(uint8_t *)(arg1) = (uint8_t)((uint32_t)(Arg2));
    *(uint16_t *)(arg1 + 0x1) = 0x600ULL;
    *(uint32_t *)(arg1 + 0x4) = Arg3;
    *(void **)(arg1 + 0x8 + 0x8) = Arg1 + 8;
    *(void **)(arg1 + 0x8) = Arg1 + 8;
    if (result == 0) goto loc_0062F960;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D4FB2)) != 0) goto loc_0062F914;
    if (((*(uint32_t *)(v_rip + 0x8D506E)) & (0x800ULL)) == 0) goto loc_0062F927;
loc_0062F914:
    result = ExAcquireRundownProtection(v_rip + 9258341, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062F960;
loc_0062F927:
    local_rsi = (result) + (48);
    goto loc_0062F94A;
loc_0062F930:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062F94A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062F930;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9258277;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x1` | `16` | `W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062F800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062F800[BB_0062F800]
  bb_0062F84B[BB_0062F84B]
  bb_0062F852[BB_0062F852]
  bb_0062F85E[BB_0062F85E]
  bb_0062F862[BB_0062F862]
  bb_0062F86C[BB_0062F86C]
  bb_0062F887[BB_0062F887]
  bb_0062F893[BB_0062F893]
  bb_0062F8A6[BB_0062F8A6]
  bb_0062F8AF[BB_0062F8AF]
  bb_0062F8B8[BB_0062F8B8]
  bb_0062F8C6[BB_0062F8C6]
  bb_0062F8C9[BB_0062F8C9]
  bb_0062F8CE[BB_0062F8CE]
  bb_0062F8D3[BB_0062F8D3]
  bb_0062F8DF[BB_0062F8DF]
  bb_0062F8FC[BB_0062F8FC]
  bb_0062F908[BB_0062F908]
  bb_0062F914[BB_0062F914]
  bb_0062F927[BB_0062F927]
  bb_0062F930[BB_0062F930]
  bb_0062F939[BB_0062F939]
  bb_0062F947[BB_0062F947]
  bb_0062F94A[BB_0062F94A]
  bb_0062F94F[BB_0062F94F]
  bb_0062F954[BB_0062F954]
  bb_0062F960[BB_0062F960]
  bb_0062F97F[BB_0062F97F]
  bb_0062F800 -->|branch| bb_0062F8DF
  bb_0062F800 -->|fallthrough| bb_0062F84B
  bb_0062F84B -->|branch| bb_0062F85E
  bb_0062F84B -->|fallthrough| bb_0062F852
  bb_0062F852 -->|branch| bb_0062F86C
  bb_0062F85E -->|branch| bb_0062F86C
  bb_0062F85E -->|fallthrough| bb_0062F862
  bb_0062F862 -->|flow| bb_0062F86C
  bb_0062F86C -->|branch| bb_0062F893
  bb_0062F86C -->|fallthrough| bb_0062F887
  bb_0062F887 -->|branch| bb_0062F8A6
  bb_0062F887 -->|fallthrough| bb_0062F893
  bb_0062F893 -->|branch| bb_0062F8DF
  bb_0062F893 -->|fallthrough| bb_0062F8A6
  bb_0062F8A6 -->|branch| bb_0062F8C9
  bb_0062F8AF -->|branch| bb_0062F8C6
  bb_0062F8AF -->|fallthrough| bb_0062F8B8
  bb_0062F8B8 -->|flow| bb_0062F8C6
  bb_0062F8C6 -->|flow| bb_0062F8C9
  bb_0062F8C9 -->|branch| bb_0062F8AF
  bb_0062F8C9 -->|fallthrough| bb_0062F8CE
  bb_0062F8CE -->|branch| bb_0062F8DF
  bb_0062F8CE -->|fallthrough| bb_0062F8D3
  bb_0062F8D3 -->|flow| bb_0062F8DF
  bb_0062F8DF -->|branch| bb_0062F960
  bb_0062F8DF -->|fallthrough| bb_0062F8FC
  bb_0062F8FC -->|branch| bb_0062F914
  bb_0062F8FC -->|fallthrough| bb_0062F908
  bb_0062F908 -->|branch| bb_0062F927
  bb_0062F908 -->|fallthrough| bb_0062F914
  bb_0062F914 -->|branch| bb_0062F960
  bb_0062F914 -->|fallthrough| bb_0062F927
  bb_0062F927 -->|branch| bb_0062F94A
  bb_0062F930 -->|branch| bb_0062F947
  bb_0062F930 -->|fallthrough| bb_0062F939
  bb_0062F939 -->|flow| bb_0062F947
  bb_0062F947 -->|flow| bb_0062F94A
  bb_0062F94A -->|branch| bb_0062F930
  bb_0062F94A -->|fallthrough| bb_0062F94F
  bb_0062F94F -->|branch| bb_0062F960
  bb_0062F94F -->|fallthrough| bb_0062F954
  bb_0062F954 -->|flow| bb_0062F960
```
