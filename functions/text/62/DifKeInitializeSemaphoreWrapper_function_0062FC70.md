# DifKeInitializeSemaphoreWrapper

- RVA: `0x0062FC70`–`0x0062FDF1` (길이 `385` bytes)
- VA: `0x000000014062FC70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `105`개 명령, `385/385` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062FCA9` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062FCD1` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062FD09` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FD30` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FD49` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062FD8C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FDB3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FDCC` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062FCE3` → RVA `0x00F048B8` (`.data`; read)
- `0x0062FCF6` → RVA `0x00F04980` (`.data`; read)
- `0x0062FD02` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062FC70  4C 8B DC                        mov r11, rsp
0062FC73  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062FC77  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062FC7B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062FC7F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062FC83  41 54                           push r12
0062FC85  41 56                           push r14
0062FC87  41 57                           push r15
0062FC89  48 83 EC 40                     sub rsp, 0x40
0062FC8D  33 C0                           xor eax, eax
0062FC8F  0F 57 C0                        xorps xmm0, xmm0
0062FC92  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062FC97  48 8B D9                        mov rbx, rcx
0062FC9A  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0062FC9E  B9 18 01 00 00                  mov ecx, 0x118
0062FCA3  45 8B F8                        mov r15d, r8d
0062FCA6  44 8B E2                        mov r12d, edx
0062FCA9  E8 86 5D E6 FF                  call 0x140495a34
0062FCAE  48 8B F0                        mov rsi, rax
0062FCB1  48 85 C0                        test rax, rax
0062FCB4  0F 84 94 00 00 00               je 0x14062fd4e
0062FCBA  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062FCBD  A8 18                           test al, 0x18
0062FCBF  74 0C                           je 0x14062fccd
0062FCC1  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062FCC6  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062FCCB  EB 0E                           jmp 0x14062fcdb
0062FCCD  A8 04                           test al, 4
0062FCCF  74 0A                           je 0x14062fcdb
0062FCD1  E8 32 3F EA FF                  call 0x1404d3c08
0062FCD6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062FCDB  40 32 ED                        xor bpl, bpl
0062FCDE  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0062FCE3  40 38 2D CE 4B 8D 00            cmp byte ptr [rip + 0x8d4bce], bpl
0062FCEA  44 89 64 24 2C                  mov dword ptr [rsp + 0x2c], r12d
0062FCEF  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
0062FCF4  75 0C                           jne 0x14062fd02
0062FCF6  F7 05 80 4C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4c80], 0x800
0062FD00  74 13                           je 0x14062fd15
0062FD02  48 8D 0D 77 41 8D 00            lea rcx, [rip + 0x8d4177]
0062FD09  E8 12 69 BE FF                  call 0x140216620
0062FD0E  40 8A E8                        mov bpl, al
0062FD11  84 C0                           test al, al
0062FD13  74 39                           je 0x14062fd4e
0062FD15  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062FD19  49 8B 3E                        mov rdi, qword ptr [r14]
0062FD1C  EB 1A                           jmp 0x14062fd38
0062FD1E  48 8D 47 F0                     lea rax, [rdi - 0x10]
0062FD22  48 85 C0                        test rax, rax
0062FD25  74 0E                           je 0x14062fd35
0062FD27  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FD2B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FD30  E8 9B AD 08 00                  call 0x1406baad0
0062FD35  48 8B 3F                        mov rdi, qword ptr [rdi]
0062FD38  49 3B FE                        cmp rdi, r14
0062FD3B  75 E1                           jne 0x14062fd1e
0062FD3D  40 84 ED                        test bpl, bpl
0062FD40  74 0C                           je 0x14062fd4e
0062FD42  48 8D 0D 37 41 8D 00            lea rcx, [rip + 0x8d4137]
0062FD49  E8 32 A1 D1 FF                  call 0x140349e80
0062FD4E  C6 03 05                        mov byte ptr [rbx], 5
0062FD51  48 8D 43 08                     lea rax, [rbx + 8]
0062FD55  C6 43 02 08                     mov byte ptr [rbx + 2], 8
0062FD59  44 89 63 04                     mov dword ptr [rbx + 4], r12d
0062FD5D  48 89 40 08                     mov qword ptr [rax + 8], rax
0062FD61  48 89 00                        mov qword ptr [rax], rax
0062FD64  44 89 7B 18                     mov dword ptr [rbx + 0x18], r15d
0062FD68  48 85 F6                        test rsi, rsi
0062FD6B  74 64                           je 0x14062fdd1
0062FD6D  40 32 FF                        xor dil, dil
0062FD70  40 38 3D 41 4B 8D 00            cmp byte ptr [rip + 0x8d4b41], dil
0062FD77  75 0C                           jne 0x14062fd85
0062FD79  F7 05 FD 4B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4bfd], 0x800
0062FD83  74 13                           je 0x14062fd98
0062FD85  48 8D 0D F4 40 8D 00            lea rcx, [rip + 0x8d40f4]
0062FD8C  E8 8F 68 BE FF                  call 0x140216620
0062FD91  40 8A F8                        mov dil, al
0062FD94  84 C0                           test al, al
0062FD96  74 39                           je 0x14062fdd1
0062FD98  48 83 C6 30                     add rsi, 0x30
0062FD9C  48 8B 1E                        mov rbx, qword ptr [rsi]
0062FD9F  EB 1A                           jmp 0x14062fdbb
0062FDA1  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062FDA5  48 85 C0                        test rax, rax
0062FDA8  74 0E                           je 0x14062fdb8
0062FDAA  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FDAE  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FDB3  E8 18 AD 08 00                  call 0x1406baad0
0062FDB8  48 8B 1B                        mov rbx, qword ptr [rbx]
0062FDBB  48 3B DE                        cmp rbx, rsi
0062FDBE  75 E1                           jne 0x14062fda1
0062FDC0  40 84 FF                        test dil, dil
0062FDC3  74 0C                           je 0x14062fdd1
0062FDC5  48 8D 0D B4 40 8D 00            lea rcx, [rip + 0x8d40b4]
0062FDCC  E8 AF A0 D1 FF                  call 0x140349e80
0062FDD1  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062FDD6  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062FDDB  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062FDE0  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062FDE5  48 83 C4 40                     add rsp, 0x40
0062FDE9  41 5F                           pop r15
0062FDEB  41 5E                           pop r14
0062FDED  41 5C                           pop r12
0062FDEF  C3                              ret
0062FDF0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInitializeSemaphoreWrapper(__int64 a1, int a2, int a3)
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
    result = DifGetAPIThunkContextById(280, a2, a3, a4);
    if (result == 0) goto loc_0062FD4E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062FCCD;
    v_stack_m38 = v_stack_p0;
    goto loc_0062FCDB;
loc_0062FCCD:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m2C = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9259982)) != 0) goto loc_0062FD02;
    if (((*(unsigned int *)(v_rip + 9260160)) & (0x800ULL)) == 0) goto loc_0062FD15;
loc_0062FD02:
    result = ExAcquireRundownProtection(v_rip + 9257335, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FD4E;
loc_0062FD15:
    goto loc_0062FD38;
loc_0062FD1E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FD38:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062FD1E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9257271;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    *(unsigned __int8 *)(a1) = 5;
    *(unsigned __int8 *)(a1 + 2) = 8;
    *(unsigned int *)(a1 + 4) = (unsigned int)((unsigned int)(a2));
    *(unsigned __int64 *)(a1 + 8 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 8) = a1 + 8;
    *(unsigned int *)(a1 + 24) = (unsigned int)((unsigned int)(a3));
    if (result == 0) goto loc_0062FDD1;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9259841)) != 0) goto loc_0062FD85;
    if (((*(unsigned int *)(v_rip + 9260029)) & (0x800ULL)) == 0) goto loc_0062FD98;
loc_0062FD85:
    result = ExAcquireRundownProtection(v_rip + 9257204, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FDD1;
loc_0062FD98:
    v_rsi = (result) + (48);
    goto loc_0062FDBB;
loc_0062FDA1:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FDBB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062FDA1;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9257140;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInitializeSemaphoreWrapper(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
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
    result = DifGetAPIThunkContextById(280, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062FD4E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062FCCD;
    v_stack_m38 = v_stack_p0;
    goto loc_0062FCDB;
loc_0062FCCD:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m2C = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8D4BCE)) != 0) goto loc_0062FD02;
    if (((*(uint32_t *)(v_rip + 0x8D4C80)) & (0x800ULL)) == 0) goto loc_0062FD15;
loc_0062FD02:
    result = ExAcquireRundownProtection(v_rip + 9257335, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062FD4E;
loc_0062FD15:
    goto loc_0062FD38;
loc_0062FD1E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062FD38:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062FD1E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9257271;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    *(uint8_t *)(arg1) = 5;
    *(uint8_t *)(arg1 + 0x2) = 8;
    *(uint32_t *)(arg1 + 0x4) = (uint32_t)((uint32_t)(Arg2));
    *(void **)(arg1 + 0x8 + 0x8) = Arg1 + 8;
    *(void **)(arg1 + 0x8) = Arg1 + 8;
    *(uint32_t *)(arg1 + 0x18) = (uint32_t)((uint32_t)(Arg3));
    if (result == 0) goto loc_0062FDD1;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D4B41)) != 0) goto loc_0062FD85;
    if (((*(uint32_t *)(v_rip + 0x8D4BFD)) & (0x800ULL)) == 0) goto loc_0062FD98;
loc_0062FD85:
    result = ExAcquireRundownProtection(v_rip + 9257204, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062FDD1;
loc_0062FD98:
    local_rsi = (result) + (48);
    goto loc_0062FDBB;
loc_0062FDA1:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062FDBB:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062FDA1;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9257140;
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
| `Arg1` | `+ 0x2` | `8` | `W` |
| `Arg1` | `+ 0x4` | `32` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062FC70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062FC70[BB_0062FC70]
  bb_0062FCBA[BB_0062FCBA]
  bb_0062FCC1[BB_0062FCC1]
  bb_0062FCCD[BB_0062FCCD]
  bb_0062FCD1[BB_0062FCD1]
  bb_0062FCDB[BB_0062FCDB]
  bb_0062FCF6[BB_0062FCF6]
  bb_0062FD02[BB_0062FD02]
  bb_0062FD15[BB_0062FD15]
  bb_0062FD1E[BB_0062FD1E]
  bb_0062FD27[BB_0062FD27]
  bb_0062FD35[BB_0062FD35]
  bb_0062FD38[BB_0062FD38]
  bb_0062FD3D[BB_0062FD3D]
  bb_0062FD42[BB_0062FD42]
  bb_0062FD4E[BB_0062FD4E]
  bb_0062FD6D[BB_0062FD6D]
  bb_0062FD79[BB_0062FD79]
  bb_0062FD85[BB_0062FD85]
  bb_0062FD98[BB_0062FD98]
  bb_0062FDA1[BB_0062FDA1]
  bb_0062FDAA[BB_0062FDAA]
  bb_0062FDB8[BB_0062FDB8]
  bb_0062FDBB[BB_0062FDBB]
  bb_0062FDC0[BB_0062FDC0]
  bb_0062FDC5[BB_0062FDC5]
  bb_0062FDD1[BB_0062FDD1]
  bb_0062FDF0[BB_0062FDF0]
  bb_0062FC70 -->|branch| bb_0062FD4E
  bb_0062FC70 -->|fallthrough| bb_0062FCBA
  bb_0062FCBA -->|branch| bb_0062FCCD
  bb_0062FCBA -->|fallthrough| bb_0062FCC1
  bb_0062FCC1 -->|branch| bb_0062FCDB
  bb_0062FCCD -->|branch| bb_0062FCDB
  bb_0062FCCD -->|fallthrough| bb_0062FCD1
  bb_0062FCD1 -->|flow| bb_0062FCDB
  bb_0062FCDB -->|branch| bb_0062FD02
  bb_0062FCDB -->|fallthrough| bb_0062FCF6
  bb_0062FCF6 -->|branch| bb_0062FD15
  bb_0062FCF6 -->|fallthrough| bb_0062FD02
  bb_0062FD02 -->|branch| bb_0062FD4E
  bb_0062FD02 -->|fallthrough| bb_0062FD15
  bb_0062FD15 -->|branch| bb_0062FD38
  bb_0062FD1E -->|branch| bb_0062FD35
  bb_0062FD1E -->|fallthrough| bb_0062FD27
  bb_0062FD27 -->|flow| bb_0062FD35
  bb_0062FD35 -->|flow| bb_0062FD38
  bb_0062FD38 -->|branch| bb_0062FD1E
  bb_0062FD38 -->|fallthrough| bb_0062FD3D
  bb_0062FD3D -->|branch| bb_0062FD4E
  bb_0062FD3D -->|fallthrough| bb_0062FD42
  bb_0062FD42 -->|flow| bb_0062FD4E
  bb_0062FD4E -->|branch| bb_0062FDD1
  bb_0062FD4E -->|fallthrough| bb_0062FD6D
  bb_0062FD6D -->|branch| bb_0062FD85
  bb_0062FD6D -->|fallthrough| bb_0062FD79
  bb_0062FD79 -->|branch| bb_0062FD98
  bb_0062FD79 -->|fallthrough| bb_0062FD85
  bb_0062FD85 -->|branch| bb_0062FDD1
  bb_0062FD85 -->|fallthrough| bb_0062FD98
  bb_0062FD98 -->|branch| bb_0062FDBB
  bb_0062FDA1 -->|branch| bb_0062FDB8
  bb_0062FDA1 -->|fallthrough| bb_0062FDAA
  bb_0062FDAA -->|flow| bb_0062FDB8
  bb_0062FDB8 -->|flow| bb_0062FDBB
  bb_0062FDBB -->|branch| bb_0062FDA1
  bb_0062FDBB -->|fallthrough| bb_0062FDC0
  bb_0062FDC0 -->|branch| bb_0062FDD1
  bb_0062FDC0 -->|fallthrough| bb_0062FDC5
  bb_0062FDC5 -->|flow| bb_0062FDD1
```
