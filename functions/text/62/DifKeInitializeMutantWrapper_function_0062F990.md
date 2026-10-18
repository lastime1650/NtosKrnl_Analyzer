# DifKeInitializeMutantWrapper

- RVA: `0x0062F990`–`0x0062FAF5` (길이 `357` bytes)
- VA: `0x000000014062F990`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `99`개 명령, `357/357` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062F9C1` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062F9E9` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062FA1C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FA43` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FA5C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062FA6D` → [KiInitializeMutant](../45/KiInitializeMutant_function_00456E9C.md) (function, `0x00456E9C`)
- `0x0062FA96` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062FABD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062FAD6` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062F9FB` → RVA `0x00F048B8` (`.data`; read)
- `0x0062FA09` → RVA `0x00F04980` (`.data`; read)
- `0x0062FA15` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062F990  4C 8B DC                        mov r11, rsp
0062F993  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062F997  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062F99B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062F99F  57                              push rdi
0062F9A0  41 56                           push r14
0062F9A2  41 57                           push r15
0062F9A4  48 83 EC 40                     sub rsp, 0x40
0062F9A8  33 C0                           xor eax, eax
0062F9AA  0F 57 C0                        xorps xmm0, xmm0
0062F9AD  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062F9B2  4C 8B F9                        mov r15, rcx
0062F9B5  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0062F9B9  B9 1A 01 00 00                  mov ecx, 0x11a
0062F9BE  44 8A F2                        mov r14b, dl
0062F9C1  E8 6E 60 E6 FF                  call 0x140495a34
0062F9C6  48 8B F0                        mov rsi, rax
0062F9C9  48 85 C0                        test rax, rax
0062F9CC  0F 84 8F 00 00 00               je 0x14062fa61
0062F9D2  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062F9D5  A8 18                           test al, 0x18
0062F9D7  74 0C                           je 0x14062f9e5
0062F9D9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062F9DE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062F9E3  EB 0E                           jmp 0x14062f9f3
0062F9E5  A8 04                           test al, 4
0062F9E7  74 0A                           je 0x14062f9f3
0062F9E9  E8 1A 42 EA FF                  call 0x1404d3c08
0062F9EE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062F9F3  40 32 ED                        xor bpl, bpl
0062F9F6  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062F9FB  40 38 2D B6 4E 8D 00            cmp byte ptr [rip + 0x8d4eb6], bpl
0062FA02  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
0062FA07  75 0C                           jne 0x14062fa15
0062FA09  F7 05 6D 4F 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4f6d], 0x800
0062FA13  74 13                           je 0x14062fa28
0062FA15  48 8D 0D 64 44 8D 00            lea rcx, [rip + 0x8d4464]
0062FA1C  E8 FF 6B BE FF                  call 0x140216620
0062FA21  40 8A E8                        mov bpl, al
0062FA24  84 C0                           test al, al
0062FA26  74 39                           je 0x14062fa61
0062FA28  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062FA2C  48 8B 1F                        mov rbx, qword ptr [rdi]
0062FA2F  EB 1A                           jmp 0x14062fa4b
0062FA31  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062FA35  48 85 C0                        test rax, rax
0062FA38  74 0E                           je 0x14062fa48
0062FA3A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FA3E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FA43  E8 88 B0 08 00                  call 0x1406baad0
0062FA48  48 8B 1B                        mov rbx, qword ptr [rbx]
0062FA4B  48 3B DF                        cmp rbx, rdi
0062FA4E  75 E1                           jne 0x14062fa31
0062FA50  40 84 ED                        test bpl, bpl
0062FA53  74 0C                           je 0x14062fa61
0062FA55  48 8D 0D 24 44 8D 00            lea rcx, [rip + 0x8d4424]
0062FA5C  E8 1F A4 D1 FF                  call 0x140349e80
0062FA61  45 33 C9                        xor r9d, r9d
0062FA64  45 33 C0                        xor r8d, r8d
0062FA67  41 8A D6                        mov dl, r14b
0062FA6A  49 8B CF                        mov rcx, r15
0062FA6D  E8 2A 74 E2 FF                  call 0x140456e9c
0062FA72  48 85 F6                        test rsi, rsi
0062FA75  74 64                           je 0x14062fadb
0062FA77  40 32 FF                        xor dil, dil
0062FA7A  40 38 3D 37 4E 8D 00            cmp byte ptr [rip + 0x8d4e37], dil
0062FA81  75 0C                           jne 0x14062fa8f
0062FA83  F7 05 F3 4E 8D 00 00 08 00 00   test dword ptr [rip + 0x8d4ef3], 0x800
0062FA8D  74 13                           je 0x14062faa2
0062FA8F  48 8D 0D EA 43 8D 00            lea rcx, [rip + 0x8d43ea]
0062FA96  E8 85 6B BE FF                  call 0x140216620
0062FA9B  40 8A F8                        mov dil, al
0062FA9E  84 C0                           test al, al
0062FAA0  74 39                           je 0x14062fadb
0062FAA2  48 83 C6 30                     add rsi, 0x30
0062FAA6  48 8B 1E                        mov rbx, qword ptr [rsi]
0062FAA9  EB 1A                           jmp 0x14062fac5
0062FAAB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062FAAF  48 85 C0                        test rax, rax
0062FAB2  74 0E                           je 0x14062fac2
0062FAB4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062FAB8  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062FABD  E8 0E B0 08 00                  call 0x1406baad0
0062FAC2  48 8B 1B                        mov rbx, qword ptr [rbx]
0062FAC5  48 3B DE                        cmp rbx, rsi
0062FAC8  75 E1                           jne 0x14062faab
0062FACA  40 84 FF                        test dil, dil
0062FACD  74 0C                           je 0x14062fadb
0062FACF  48 8D 0D AA 43 8D 00            lea rcx, [rip + 0x8d43aa]
0062FAD6  E8 A5 A3 D1 FF                  call 0x140349e80
0062FADB  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062FAE0  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062FAE5  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062FAEA  48 83 C4 40                     add rsp, 0x40
0062FAEE  41 5F                           pop r15
0062FAF0  41 5E                           pop r14
0062FAF2  5F                              pop rdi
0062FAF3  C3                              ret
0062FAF4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeInitializeMutantWrapper(__int64 a1, unsigned __int8 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = 0;
    result = DifGetAPIThunkContextById(282, a2, a3, a4);
    if (result == 0) goto loc_0062FA61;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062F9E5;
    v_stack_m38 = v_stack_p0;
    goto loc_0062F9F3;
loc_0062F9E5:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9260726)) != 0) goto loc_0062FA15;
    if (((*(unsigned int *)(v_rip + 9260909)) & (0x800ULL)) == 0) goto loc_0062FA28;
loc_0062FA15:
    result = ExAcquireRundownProtection(v_rip + 9258084, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FA61;
loc_0062FA28:
    goto loc_0062FA4B;
loc_0062FA31:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FA4B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062FA31;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9258020;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a4 = 0;
    a3 = 0;
    result = KiInitializeMutant(a1, a2, a3, a4);
    if (result == 0) goto loc_0062FADB;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9260599)) != 0) goto loc_0062FA8F;
    if (((*(unsigned int *)(v_rip + 9260787)) & (0x800ULL)) == 0) goto loc_0062FAA2;
loc_0062FA8F:
    result = ExAcquireRundownProtection(v_rip + 9257962, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062FADB;
loc_0062FAA2:
    v_rsi = (result) + (48);
    goto loc_0062FAC5;
loc_0062FAAB:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062FAC5:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062FAAB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9257898;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeInitializeMutantWrapper(int64_t Arg1, uint8_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m38 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = 0;
    result = DifGetAPIThunkContextById(282, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062FA61;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062F9E5;
    v_stack_m38 = v_stack_p0;
    goto loc_0062F9F3;
loc_0062F9E5:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D4EB6)) != 0) goto loc_0062FA15;
    if (((*(uint32_t *)(v_rip + 0x8D4F6D)) & (0x800ULL)) == 0) goto loc_0062FA28;
loc_0062FA15:
    result = ExAcquireRundownProtection(v_rip + 9258084, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062FA61;
loc_0062FA28:
    goto loc_0062FA4B;
loc_0062FA31:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062FA4B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062FA31;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9258020;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    Arg4 = 0;
    Arg3 = 0;
    result = KiInitializeMutant(Arg1, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062FADB;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D4E37)) != 0) goto loc_0062FA8F;
    if (((*(uint32_t *)(v_rip + 0x8D4EF3)) & (0x800ULL)) == 0) goto loc_0062FAA2;
loc_0062FA8F:
    result = ExAcquireRundownProtection(v_rip + 9257962, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062FADB;
loc_0062FAA2:
    local_rsi = (result) + (48);
    goto loc_0062FAC5;
loc_0062FAAB:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0062FAC5:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062FAAB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9257898;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062F990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062F990[BB_0062F990]
  bb_0062F9D2[BB_0062F9D2]
  bb_0062F9D9[BB_0062F9D9]
  bb_0062F9E5[BB_0062F9E5]
  bb_0062F9E9[BB_0062F9E9]
  bb_0062F9F3[BB_0062F9F3]
  bb_0062FA09[BB_0062FA09]
  bb_0062FA15[BB_0062FA15]
  bb_0062FA28[BB_0062FA28]
  bb_0062FA31[BB_0062FA31]
  bb_0062FA3A[BB_0062FA3A]
  bb_0062FA48[BB_0062FA48]
  bb_0062FA4B[BB_0062FA4B]
  bb_0062FA50[BB_0062FA50]
  bb_0062FA55[BB_0062FA55]
  bb_0062FA61[BB_0062FA61]
  bb_0062FA77[BB_0062FA77]
  bb_0062FA83[BB_0062FA83]
  bb_0062FA8F[BB_0062FA8F]
  bb_0062FAA2[BB_0062FAA2]
  bb_0062FAAB[BB_0062FAAB]
  bb_0062FAB4[BB_0062FAB4]
  bb_0062FAC2[BB_0062FAC2]
  bb_0062FAC5[BB_0062FAC5]
  bb_0062FACA[BB_0062FACA]
  bb_0062FACF[BB_0062FACF]
  bb_0062FADB[BB_0062FADB]
  bb_0062FAF4[BB_0062FAF4]
  bb_0062F990 -->|branch| bb_0062FA61
  bb_0062F990 -->|fallthrough| bb_0062F9D2
  bb_0062F9D2 -->|branch| bb_0062F9E5
  bb_0062F9D2 -->|fallthrough| bb_0062F9D9
  bb_0062F9D9 -->|branch| bb_0062F9F3
  bb_0062F9E5 -->|branch| bb_0062F9F3
  bb_0062F9E5 -->|fallthrough| bb_0062F9E9
  bb_0062F9E9 -->|flow| bb_0062F9F3
  bb_0062F9F3 -->|branch| bb_0062FA15
  bb_0062F9F3 -->|fallthrough| bb_0062FA09
  bb_0062FA09 -->|branch| bb_0062FA28
  bb_0062FA09 -->|fallthrough| bb_0062FA15
  bb_0062FA15 -->|branch| bb_0062FA61
  bb_0062FA15 -->|fallthrough| bb_0062FA28
  bb_0062FA28 -->|branch| bb_0062FA4B
  bb_0062FA31 -->|branch| bb_0062FA48
  bb_0062FA31 -->|fallthrough| bb_0062FA3A
  bb_0062FA3A -->|flow| bb_0062FA48
  bb_0062FA48 -->|flow| bb_0062FA4B
  bb_0062FA4B -->|branch| bb_0062FA31
  bb_0062FA4B -->|fallthrough| bb_0062FA50
  bb_0062FA50 -->|branch| bb_0062FA61
  bb_0062FA50 -->|fallthrough| bb_0062FA55
  bb_0062FA55 -->|flow| bb_0062FA61
  bb_0062FA61 -->|branch| bb_0062FADB
  bb_0062FA61 -->|fallthrough| bb_0062FA77
  bb_0062FA77 -->|branch| bb_0062FA8F
  bb_0062FA77 -->|fallthrough| bb_0062FA83
  bb_0062FA83 -->|branch| bb_0062FAA2
  bb_0062FA83 -->|fallthrough| bb_0062FA8F
  bb_0062FA8F -->|branch| bb_0062FADB
  bb_0062FA8F -->|fallthrough| bb_0062FAA2
  bb_0062FAA2 -->|branch| bb_0062FAC5
  bb_0062FAAB -->|branch| bb_0062FAC2
  bb_0062FAAB -->|fallthrough| bb_0062FAB4
  bb_0062FAB4 -->|flow| bb_0062FAC2
  bb_0062FAC2 -->|flow| bb_0062FAC5
  bb_0062FAC5 -->|branch| bb_0062FAAB
  bb_0062FAC5 -->|fallthrough| bb_0062FACA
  bb_0062FACA -->|branch| bb_0062FADB
  bb_0062FACA -->|fallthrough| bb_0062FACF
  bb_0062FACF -->|flow| bb_0062FADB
```
