# DifKeInitializeTimerExWrapper

- RVA: `0x0062FE00`–`0x0062FF84` (길이 `388` bytes)
- VA: `0x000000014062FE00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `106`개 명령, `388/388` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062FE36` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062FE61` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062FE94` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FEBB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FED4` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062FF1F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FF46` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FF5F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062FE6B` → RVA `0x00F048B8` (`.data`; read)
- `0x0062FE81` → RVA `0x00F04980` (`.data`; read)
- `0x0062FE8D` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062FE00  4C 8B DC                        mov r11, rsp
0062FE03  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062FE07  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062FE0B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062FE0F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062FE13  41 54                           push r12
0062FE15  41 56                           push r14
0062FE17  41 57                           push r15
0062FE19  48 83 EC 40                     sub rsp, 0x40
0062FE1D  33 C0                           xor eax, eax
0062FE1F  0F 57 C0                        xorps xmm0, xmm0
0062FE22  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062FE27  48 8B D9                        mov rbx, rcx
0062FE2A  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0062FE2E  B9 16 01 00 00                  mov ecx, 0x116
0062FE33  44 8B FA                        mov r15d, edx
0062FE36  E8 F9 5B E6 FF                  call 0x140495a34
0062FE3B  45 33 E4                        xor r12d, r12d
0062FE3E  48 8B F0                        mov rsi, rax
0062FE41  48 85 C0                        test rax, rax
0062FE44  0F 84 8F 00 00 00               je 0x14062fed9
0062FE4A  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062FE4D  A8 18                           test al, 0x18
0062FE4F  74 0C                           je 0x14062fe5d
0062FE51  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062FE56  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062FE5B  EB 0E                           jmp 0x14062fe6b
0062FE5D  A8 04                           test al, 4
0062FE5F  74 0A                           je 0x14062fe6b
0062FE61  E8 A2 3D EA FF                  call 0x1404d3c08
0062FE66  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062FE6B  44 38 25 46 4A 8D 00            cmp byte ptr [rip + 0x8d4a46], r12b
0062FE72  41 8A EC                        mov bpl, r12b
0062FE75  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0062FE7A  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
0062FE7F  75 0C                           jne 0x14062fe8d
0062FE81  F7 05 F5 4A 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4af5], 0x800
0062FE8B  74 13                           je 0x14062fea0
0062FE8D  48 8D 0D EC 3F 8D 00            lea rcx, [rip + 0x8d3fec]
0062FE94  E8 87 67 BE FF                  call 0x140216620
0062FE99  40 8A E8                        mov bpl, al
0062FE9C  84 C0                           test al, al
0062FE9E  74 39                           je 0x14062fed9
0062FEA0  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062FEA4  49 8B 3E                        mov rdi, qword ptr [r14]
0062FEA7  EB 1A                           jmp 0x14062fec3
0062FEA9  48 8D 47 F0                     lea rax, [rdi - 0x10]
0062FEAD  48 85 C0                        test rax, rax
0062FEB0  74 0E                           je 0x14062fec0
0062FEB2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FEB6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FEBB  E8 10 AC 08 00                  call 0x1406baad0
0062FEC0  48 8B 3F                        mov rdi, qword ptr [rdi]
0062FEC3  49 3B FE                        cmp rdi, r14
0062FEC6  75 E1                           jne 0x14062fea9
0062FEC8  40 84 ED                        test bpl, bpl
0062FECB  74 0C                           je 0x14062fed9
0062FECD  48 8D 0D AC 3F 8D 00            lea rcx, [rip + 0x8d3fac]
0062FED4  E8 A7 9F D1 FF                  call 0x140349e80
0062FED9  4C 89 23                        mov qword ptr [rbx], r12
0062FEDC  48 8D 43 08                     lea rax, [rbx + 8]
0062FEE0  41 80 C7 08                     add r15b, 8
0062FEE4  44 88 3B                        mov byte ptr [rbx], r15b
0062FEE7  48 89 40 08                     mov qword ptr [rax + 8], rax
0062FEEB  48 89 00                        mov qword ptr [rax], rax
0062FEEE  4C 89 63 18                     mov qword ptr [rbx + 0x18], r12
0062FEF2  44 89 63 3C                     mov dword ptr [rbx + 0x3c], r12d
0062FEF6  66 44 89 63 38                  mov word ptr [rbx + 0x38], r12w
0062FEFB  48 85 F6                        test rsi, rsi
0062FEFE  74 64                           je 0x14062ff64
0062FF00  44 38 25 B1 49 8D 00            cmp byte ptr [rip + 0x8d49b1], r12b
0062FF07  41 8A FC                        mov dil, r12b
0062FF0A  75 0C                           jne 0x14062ff18
0062FF0C  F7 05 6A 4A 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4a6a], 0x800
0062FF16  74 13                           je 0x14062ff2b
0062FF18  48 8D 0D 61 3F 8D 00            lea rcx, [rip + 0x8d3f61]
0062FF1F  E8 FC 66 BE FF                  call 0x140216620
0062FF24  40 8A F8                        mov dil, al
0062FF27  84 C0                           test al, al
0062FF29  74 39                           je 0x14062ff64
0062FF2B  48 83 C6 30                     add rsi, 0x30
0062FF2F  48 8B 1E                        mov rbx, qword ptr [rsi]
0062FF32  EB 1A                           jmp 0x14062ff4e
0062FF34  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062FF38  48 85 C0                        test rax, rax
0062FF3B  74 0E                           je 0x14062ff4b
0062FF3D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FF41  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FF46  E8 85 AB 08 00                  call 0x1406baad0
0062FF4B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062FF4E  48 3B DE                        cmp rbx, rsi
0062FF51  75 E1                           jne 0x14062ff34
0062FF53  40 84 FF                        test dil, dil
0062FF56  74 0C                           je 0x14062ff64
0062FF58  48 8D 0D 21 3F 8D 00            lea rcx, [rip + 0x8d3f21]
0062FF5F  E8 1C 9F D1 FF                  call 0x140349e80
0062FF64  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062FF69  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062FF6E  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062FF73  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062FF78  48 83 C4 40                     add rsp, 0x40
0062FF7C  41 5F                           pop r15
0062FF7E  41 5E                           pop r14
0062FF80  41 5C                           pop r12
0062FF82  C3                              ret
0062FF83  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInitializeTimerExWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
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
    result = DifGetAPIThunkContextById(278, a2, a3, a4);
    v_r12 = 0;
    if (result == 0) goto loc_0062FED9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062FE5D;
    v_stack_m38 = v_stack_p0;
    goto loc_0062FE6B;
loc_0062FE5D:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9259590)) != 0) goto loc_0062FE8D;
    if (((*(unsigned int *)(v_rip + 9259765)) & (0x800ULL)) == 0) goto loc_0062FEA0;
loc_0062FE8D:
    result = ExAcquireRundownProtection(v_rip + 9256940, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FED9;
loc_0062FEA0:
    goto loc_0062FEC3;
loc_0062FEA9:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FEC3:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062FEA9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9256876;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a1) = 0;
    v_r15 = (unsigned __int8)(((unsigned int)(a2)) + (8));
    *(unsigned __int8 *)(a1) = (unsigned __int8)(v_r15);
    *(unsigned __int64 *)(a1 + 8 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 24) = 0;
    *(unsigned int *)(a1 + 60) = 0;
    *(unsigned __int16 *)(a1 + 56) = 0;
    if (result == 0) goto loc_0062FF64;
    if ((*(unsigned __int8 *)(v_rip + 9259441)) != 0) goto loc_0062FF18;
    if (((*(unsigned int *)(v_rip + 9259626)) & (0x800ULL)) == 0) goto loc_0062FF2B;
loc_0062FF18:
    result = ExAcquireRundownProtection(v_rip + 9256801, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FF64;
loc_0062FF2B:
    v_rsi = (result) + (48);
    goto loc_0062FF4E;
loc_0062FF34:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FF4E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062FF34;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9256737;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInitializeTimerExWrapper(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(278, Arg2, a3, a4);
    local_r12 = 0;
    if (result == 0) goto loc_0062FED9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062FE5D;
    v_stack_m38 = v_stack_p0;
    goto loc_0062FE6B;
loc_0062FE5D:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8D4A46)) != 0) goto loc_0062FE8D;
    if (((*(uint32_t *)(v_rip + 0x8D4AF5)) & (0x800ULL)) == 0) goto loc_0062FEA0;
loc_0062FE8D:
    result = ExAcquireRundownProtection(v_rip + 9256940, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062FED9;
loc_0062FEA0:
    goto loc_0062FEC3;
loc_0062FEA9:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062FEC3:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062FEA9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9256876;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(arg1) = 0;
    local_r15 = (uint8_t)(((uint32_t)(Arg2)) + (8));
    *(uint8_t *)(arg1) = (uint8_t)(local_r15);
    *(void **)(arg1 + 0x8 + 0x8) = Arg1 + 8;
    *(void **)(arg1 + 0x8) = Arg1 + 8;
    *(uint64_t *)(arg1 + 0x18) = 0;
    *(uint32_t *)(arg1 + 0x3C) = 0;
    *(uint16_t *)(arg1 + 0x38) = 0;
    if (result == 0) goto loc_0062FF64;
    if ((*(uint8_t *)(v_rip + 0x8D49B1)) != 0) goto loc_0062FF18;
    if (((*(uint32_t *)(v_rip + 0x8D4A6A)) & (0x800ULL)) == 0) goto loc_0062FF2B;
loc_0062FF18:
    result = ExAcquireRundownProtection(v_rip + 9256801, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062FF64;
loc_0062FF2B:
    local_rsi = (result) + (48);
    goto loc_0062FF4E;
loc_0062FF34:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062FF4E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062FF34;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9256737;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
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
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x38` | `16` | `W` |
| `Arg1` | `+ 0x3C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062FE00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062FE00[BB_0062FE00]
  bb_0062FE4A[BB_0062FE4A]
  bb_0062FE51[BB_0062FE51]
  bb_0062FE5D[BB_0062FE5D]
  bb_0062FE61[BB_0062FE61]
  bb_0062FE6B[BB_0062FE6B]
  bb_0062FE81[BB_0062FE81]
  bb_0062FE8D[BB_0062FE8D]
  bb_0062FEA0[BB_0062FEA0]
  bb_0062FEA9[BB_0062FEA9]
  bb_0062FEB2[BB_0062FEB2]
  bb_0062FEC0[BB_0062FEC0]
  bb_0062FEC3[BB_0062FEC3]
  bb_0062FEC8[BB_0062FEC8]
  bb_0062FECD[BB_0062FECD]
  bb_0062FED9[BB_0062FED9]
  bb_0062FF00[BB_0062FF00]
  bb_0062FF0C[BB_0062FF0C]
  bb_0062FF18[BB_0062FF18]
  bb_0062FF2B[BB_0062FF2B]
  bb_0062FF34[BB_0062FF34]
  bb_0062FF3D[BB_0062FF3D]
  bb_0062FF4B[BB_0062FF4B]
  bb_0062FF4E[BB_0062FF4E]
  bb_0062FF53[BB_0062FF53]
  bb_0062FF58[BB_0062FF58]
  bb_0062FF64[BB_0062FF64]
  bb_0062FF83[BB_0062FF83]
  bb_0062FE00 -->|branch| bb_0062FED9
  bb_0062FE00 -->|fallthrough| bb_0062FE4A
  bb_0062FE4A -->|branch| bb_0062FE5D
  bb_0062FE4A -->|fallthrough| bb_0062FE51
  bb_0062FE51 -->|branch| bb_0062FE6B
  bb_0062FE5D -->|branch| bb_0062FE6B
  bb_0062FE5D -->|fallthrough| bb_0062FE61
  bb_0062FE61 -->|flow| bb_0062FE6B
  bb_0062FE6B -->|branch| bb_0062FE8D
  bb_0062FE6B -->|fallthrough| bb_0062FE81
  bb_0062FE81 -->|branch| bb_0062FEA0
  bb_0062FE81 -->|fallthrough| bb_0062FE8D
  bb_0062FE8D -->|branch| bb_0062FED9
  bb_0062FE8D -->|fallthrough| bb_0062FEA0
  bb_0062FEA0 -->|branch| bb_0062FEC3
  bb_0062FEA9 -->|branch| bb_0062FEC0
  bb_0062FEA9 -->|fallthrough| bb_0062FEB2
  bb_0062FEB2 -->|flow| bb_0062FEC0
  bb_0062FEC0 -->|flow| bb_0062FEC3
  bb_0062FEC3 -->|branch| bb_0062FEA9
  bb_0062FEC3 -->|fallthrough| bb_0062FEC8
  bb_0062FEC8 -->|branch| bb_0062FED9
  bb_0062FEC8 -->|fallthrough| bb_0062FECD
  bb_0062FECD -->|flow| bb_0062FED9
  bb_0062FED9 -->|branch| bb_0062FF64
  bb_0062FED9 -->|fallthrough| bb_0062FF00
  bb_0062FF00 -->|branch| bb_0062FF18
  bb_0062FF00 -->|fallthrough| bb_0062FF0C
  bb_0062FF0C -->|branch| bb_0062FF2B
  bb_0062FF0C -->|fallthrough| bb_0062FF18
  bb_0062FF18 -->|branch| bb_0062FF64
  bb_0062FF18 -->|fallthrough| bb_0062FF2B
  bb_0062FF2B -->|branch| bb_0062FF4E
  bb_0062FF34 -->|branch| bb_0062FF4B
  bb_0062FF34 -->|fallthrough| bb_0062FF3D
  bb_0062FF3D -->|flow| bb_0062FF4B
  bb_0062FF4B -->|flow| bb_0062FF4E
  bb_0062FF4E -->|branch| bb_0062FF34
  bb_0062FF4E -->|fallthrough| bb_0062FF53
  bb_0062FF53 -->|branch| bb_0062FF64
  bb_0062FF53 -->|fallthrough| bb_0062FF58
  bb_0062FF58 -->|flow| bb_0062FF64
```
