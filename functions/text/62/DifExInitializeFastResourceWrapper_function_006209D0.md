# DifExInitializeFastResourceWrapper

- RVA: `0x006209D0`–`0x00620B33` (길이 `355` bytes)
- VA: `0x00000001406209D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `355/355` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00620A01` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00620A29` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00620A5C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620A83` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620A9C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00620AAB` → [ExInitializeFastResource2](../49/ExInitializeFastResource2_function_0049AF90.md) (function, `0x0049AF90`)
- `0x00620AD4` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620AFB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620B14` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00620A3B` → RVA `0x00F048B8` (`.data`; read)
- `0x00620A49` → RVA `0x00F04980` (`.data`; read)
- `0x00620A55` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006209D0  4C 8B DC                        mov r11, rsp
006209D3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006209D7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006209DB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006209DF  57                              push rdi
006209E0  41 56                           push r14
006209E2  41 57                           push r15
006209E4  48 83 EC 40                     sub rsp, 0x40
006209E8  33 C0                           xor eax, eax
006209EA  0F 57 C0                        xorps xmm0, xmm0
006209ED  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006209F2  4C 8B F9                        mov r15, rcx
006209F5  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
006209F9  B9 BE 01 00 00                  mov ecx, 0x1be
006209FE  44 8B F2                        mov r14d, edx
00620A01  E8 2E 50 E7 FF                  call 0x140495a34
00620A06  48 8B F0                        mov rsi, rax
00620A09  48 85 C0                        test rax, rax
00620A0C  0F 84 8F 00 00 00               je 0x140620aa1
00620A12  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00620A15  A8 18                           test al, 0x18
00620A17  74 0C                           je 0x140620a25
00620A19  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00620A1E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00620A23  EB 0E                           jmp 0x140620a33
00620A25  A8 04                           test al, 4
00620A27  74 0A                           je 0x140620a33
00620A29  E8 DA 31 EB FF                  call 0x1404d3c08
00620A2E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00620A33  40 32 ED                        xor bpl, bpl
00620A36  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00620A3B  40 38 2D 76 3E 8E 00            cmp byte ptr [rip + 0x8e3e76], bpl
00620A42  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00620A47  75 0C                           jne 0x140620a55
00620A49  F7 05 2D 3F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e3f2d], 0x800
00620A53  74 13                           je 0x140620a68
00620A55  48 8D 0D 24 34 8E 00            lea rcx, [rip + 0x8e3424]
00620A5C  E8 BF 5B BF FF                  call 0x140216620
00620A61  40 8A E8                        mov bpl, al
00620A64  84 C0                           test al, al
00620A66  74 39                           je 0x140620aa1
00620A68  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00620A6C  48 8B 1F                        mov rbx, qword ptr [rdi]
00620A6F  EB 1A                           jmp 0x140620a8b
00620A71  48 8D 43 F0                     lea rax, [rbx - 0x10]
00620A75  48 85 C0                        test rax, rax
00620A78  74 0E                           je 0x140620a88
00620A7A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620A7E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620A83  E8 48 A0 09 00                  call 0x1406baad0
00620A88  48 8B 1B                        mov rbx, qword ptr [rbx]
00620A8B  48 3B DF                        cmp rbx, rdi
00620A8E  75 E1                           jne 0x140620a71
00620A90  40 84 ED                        test bpl, bpl
00620A93  74 0C                           je 0x140620aa1
00620A95  48 8D 0D E4 33 8E 00            lea rcx, [rip + 0x8e33e4]
00620A9C  E8 DF 93 D2 FF                  call 0x140349e80
00620AA1  41 83 C8 FF                     or r8d, 0xffffffff
00620AA5  41 8B D6                        mov edx, r14d
00620AA8  49 8B CF                        mov rcx, r15
00620AAB  E8 E0 A4 E7 FF                  call 0x14049af90
00620AB0  48 85 F6                        test rsi, rsi
00620AB3  74 64                           je 0x140620b19
00620AB5  40 32 FF                        xor dil, dil
00620AB8  40 38 3D F9 3D 8E 00            cmp byte ptr [rip + 0x8e3df9], dil
00620ABF  75 0C                           jne 0x140620acd
00620AC1  F7 05 B5 3E 8E 00 00 08 00 00   test dword ptr [rip + 0x8e3eb5], 0x800
00620ACB  74 13                           je 0x140620ae0
00620ACD  48 8D 0D AC 33 8E 00            lea rcx, [rip + 0x8e33ac]
00620AD4  E8 47 5B BF FF                  call 0x140216620
00620AD9  40 8A F8                        mov dil, al
00620ADC  84 C0                           test al, al
00620ADE  74 39                           je 0x140620b19
00620AE0  48 83 C6 30                     add rsi, 0x30
00620AE4  48 8B 1E                        mov rbx, qword ptr [rsi]
00620AE7  EB 1A                           jmp 0x140620b03
00620AE9  48 8D 43 F0                     lea rax, [rbx - 0x10]
00620AED  48 85 C0                        test rax, rax
00620AF0  74 0E                           je 0x140620b00
00620AF2  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620AF6  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620AFB  E8 D0 9F 09 00                  call 0x1406baad0
00620B00  48 8B 1B                        mov rbx, qword ptr [rbx]
00620B03  48 3B DE                        cmp rbx, rsi
00620B06  75 E1                           jne 0x140620ae9
00620B08  40 84 FF                        test dil, dil
00620B0B  74 0C                           je 0x140620b19
00620B0D  48 8D 0D 6C 33 8E 00            lea rcx, [rip + 0x8e336c]
00620B14  E8 67 93 D2 FF                  call 0x140349e80
00620B19  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00620B1E  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00620B23  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00620B28  48 83 C4 40                     add rsp, 0x40
00620B2C  41 5F                           pop r15
00620B2E  41 5E                           pop r14
00620B30  5F                              pop rdi
00620B31  C3                              ret
00620B32  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExInitializeFastResourceWrapper(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
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
    result = DifGetAPIThunkContextById(446, a2, a3, a4);
    if (result == 0) goto loc_00620AA1;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00620A25;
    v_stack_m38 = v_stack_p0;
    goto loc_00620A33;
loc_00620A25:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9322102)) != 0) goto loc_00620A55;
    if (((*(unsigned int *)(v_rip + 9322285)) & (0x800ULL)) == 0) goto loc_00620A68;
loc_00620A55:
    result = ExAcquireRundownProtection(v_rip + 9319460, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00620AA1;
loc_00620A68:
    goto loc_00620A8B;
loc_00620A71:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00620A8B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00620A71;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9319396;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = ExInitializeFastResource2(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_00620B19;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9321977)) != 0) goto loc_00620ACD;
    if (((*(unsigned int *)(v_rip + 9322165)) & (0x800ULL)) == 0) goto loc_00620AE0;
loc_00620ACD:
    result = ExAcquireRundownProtection(v_rip + 9319340, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00620B19;
loc_00620AE0:
    v_rsi = (result) + (48);
    goto loc_00620B03;
loc_00620AE9:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_00620B03:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00620AE9;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9319276;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExInitializeFastResourceWrapper(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(446, Arg2, Arg3, a4);
    if (result == 0) goto loc_00620AA1;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00620A25;
    v_stack_m38 = v_stack_p0;
    goto loc_00620A33;
loc_00620A25:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8E3E76)) != 0) goto loc_00620A55;
    if (((*(uint32_t *)(v_rip + 0x8E3F2D)) & (0x800ULL)) == 0) goto loc_00620A68;
loc_00620A55:
    result = ExAcquireRundownProtection(v_rip + 9319460, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00620AA1;
loc_00620A68:
    goto loc_00620A8B;
loc_00620A71:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00620A8B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00620A71;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9319396;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    result = ExInitializeFastResource2(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if (result == 0) goto loc_00620B19;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E3DF9)) != 0) goto loc_00620ACD;
    if (((*(uint32_t *)(v_rip + 0x8E3EB5)) & (0x800ULL)) == 0) goto loc_00620AE0;
loc_00620ACD:
    result = ExAcquireRundownProtection(v_rip + 9319340, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00620B19;
loc_00620AE0:
    local_rsi = (result) + (48);
    goto loc_00620B03;
loc_00620AE9:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_00620B03:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00620AE9;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9319276;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006209D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006209D0[BB_006209D0]
  bb_00620A12[BB_00620A12]
  bb_00620A19[BB_00620A19]
  bb_00620A25[BB_00620A25]
  bb_00620A29[BB_00620A29]
  bb_00620A33[BB_00620A33]
  bb_00620A49[BB_00620A49]
  bb_00620A55[BB_00620A55]
  bb_00620A68[BB_00620A68]
  bb_00620A71[BB_00620A71]
  bb_00620A7A[BB_00620A7A]
  bb_00620A88[BB_00620A88]
  bb_00620A8B[BB_00620A8B]
  bb_00620A90[BB_00620A90]
  bb_00620A95[BB_00620A95]
  bb_00620AA1[BB_00620AA1]
  bb_00620AB5[BB_00620AB5]
  bb_00620AC1[BB_00620AC1]
  bb_00620ACD[BB_00620ACD]
  bb_00620AE0[BB_00620AE0]
  bb_00620AE9[BB_00620AE9]
  bb_00620AF2[BB_00620AF2]
  bb_00620B00[BB_00620B00]
  bb_00620B03[BB_00620B03]
  bb_00620B08[BB_00620B08]
  bb_00620B0D[BB_00620B0D]
  bb_00620B19[BB_00620B19]
  bb_00620B32[BB_00620B32]
  bb_006209D0 -->|branch| bb_00620AA1
  bb_006209D0 -->|fallthrough| bb_00620A12
  bb_00620A12 -->|branch| bb_00620A25
  bb_00620A12 -->|fallthrough| bb_00620A19
  bb_00620A19 -->|branch| bb_00620A33
  bb_00620A25 -->|branch| bb_00620A33
  bb_00620A25 -->|fallthrough| bb_00620A29
  bb_00620A29 -->|flow| bb_00620A33
  bb_00620A33 -->|branch| bb_00620A55
  bb_00620A33 -->|fallthrough| bb_00620A49
  bb_00620A49 -->|branch| bb_00620A68
  bb_00620A49 -->|fallthrough| bb_00620A55
  bb_00620A55 -->|branch| bb_00620AA1
  bb_00620A55 -->|fallthrough| bb_00620A68
  bb_00620A68 -->|branch| bb_00620A8B
  bb_00620A71 -->|branch| bb_00620A88
  bb_00620A71 -->|fallthrough| bb_00620A7A
  bb_00620A7A -->|flow| bb_00620A88
  bb_00620A88 -->|flow| bb_00620A8B
  bb_00620A8B -->|branch| bb_00620A71
  bb_00620A8B -->|fallthrough| bb_00620A90
  bb_00620A90 -->|branch| bb_00620AA1
  bb_00620A90 -->|fallthrough| bb_00620A95
  bb_00620A95 -->|flow| bb_00620AA1
  bb_00620AA1 -->|branch| bb_00620B19
  bb_00620AA1 -->|fallthrough| bb_00620AB5
  bb_00620AB5 -->|branch| bb_00620ACD
  bb_00620AB5 -->|fallthrough| bb_00620AC1
  bb_00620AC1 -->|branch| bb_00620AE0
  bb_00620AC1 -->|fallthrough| bb_00620ACD
  bb_00620ACD -->|branch| bb_00620B19
  bb_00620ACD -->|fallthrough| bb_00620AE0
  bb_00620AE0 -->|branch| bb_00620B03
  bb_00620AE9 -->|branch| bb_00620B00
  bb_00620AE9 -->|fallthrough| bb_00620AF2
  bb_00620AF2 -->|flow| bb_00620B00
  bb_00620B00 -->|flow| bb_00620B03
  bb_00620B03 -->|branch| bb_00620AE9
  bb_00620B03 -->|fallthrough| bb_00620B08
  bb_00620B08 -->|branch| bb_00620B19
  bb_00620B08 -->|fallthrough| bb_00620B0D
  bb_00620B0D -->|flow| bb_00620B19
```
