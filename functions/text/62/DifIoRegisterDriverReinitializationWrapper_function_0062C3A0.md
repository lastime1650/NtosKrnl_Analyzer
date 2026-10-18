# DifIoRegisterDriverReinitializationWrapper

- RVA: `0x0062C3A0`–`0x0062C512` (길이 `370` bytes)
- VA: `0x000000014062C3A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062C3D6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062C3FE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062C436` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C45D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C476` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062C484` → [IoRegisterDriverReinitialization](../../page/71/IoRegisterDriverReinitialization_function_0071D640.md) (function, `0x0071D640`)
- `0x0062C4AD` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062C4D4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062C4ED` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062C410` → RVA `0x00F048B8` (`.data`; read)
- `0x0062C423` → RVA `0x00F04980` (`.data`; read)
- `0x0062C42F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062C484` → [IoRegisterDriverReinitialization](../../page/71/IoRegisterDriverReinitialization_function_0071D640.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062C3A0  48 8B C4                        mov rax, rsp
0062C3A3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062C3A7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062C3AB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062C3AF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062C3B3  41 54                           push r12
0062C3B5  41 56                           push r14
0062C3B7  41 57                           push r15
0062C3B9  48 83 EC 40                     sub rsp, 0x40
0062C3BD  0F 57 C0                        xorps xmm0, xmm0
0062C3C0  4C 8B E1                        mov r12, rcx
0062C3C3  B9 3F 01 00 00                  mov ecx, 0x13f
0062C3C8  4D 8B F0                        mov r14, r8
0062C3CB  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062C3CF  4C 8B FA                        mov r15, rdx
0062C3D2  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062C3D6  E8 59 96 E6 FF                  call 0x140495a34
0062C3DB  48 8B F0                        mov rsi, rax
0062C3DE  48 85 C0                        test rax, rax
0062C3E1  0F 84 94 00 00 00               je 0x14062c47b
0062C3E7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062C3EA  A8 18                           test al, 0x18
0062C3EC  74 0C                           je 0x14062c3fa
0062C3EE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062C3F3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062C3F8  EB 0E                           jmp 0x14062c408
0062C3FA  A8 04                           test al, 4
0062C3FC  74 0A                           je 0x14062c408
0062C3FE  E8 05 78 EA FF                  call 0x1404d3c08
0062C403  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062C408  40 32 ED                        xor bpl, bpl
0062C40B  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
0062C410  40 38 2D A1 84 8D 00            cmp byte ptr [rip + 0x8d84a1], bpl
0062C417  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062C41C  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
0062C421  75 0C                           jne 0x14062c42f
0062C423  F7 05 53 85 8D 00 00 08 00 00   test dword ptr [rip + 0x8d8553], 0x800
0062C42D  74 13                           je 0x14062c442
0062C42F  48 8D 0D 4A 7A 8D 00            lea rcx, [rip + 0x8d7a4a]
0062C436  E8 E5 A1 BE FF                  call 0x140216620
0062C43B  40 8A E8                        mov bpl, al
0062C43E  84 C0                           test al, al
0062C440  74 39                           je 0x14062c47b
0062C442  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062C446  48 8B 1F                        mov rbx, qword ptr [rdi]
0062C449  EB 1A                           jmp 0x14062c465
0062C44B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C44F  48 85 C0                        test rax, rax
0062C452  74 0E                           je 0x14062c462
0062C454  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C458  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C45D  E8 6E E6 08 00                  call 0x1406baad0
0062C462  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C465  48 3B DF                        cmp rbx, rdi
0062C468  75 E1                           jne 0x14062c44b
0062C46A  40 84 ED                        test bpl, bpl
0062C46D  74 0C                           je 0x14062c47b
0062C46F  48 8D 0D 0A 7A 8D 00            lea rcx, [rip + 0x8d7a0a]
0062C476  E8 05 DA D1 FF                  call 0x140349e80
0062C47B  4D 8B C6                        mov r8, r14
0062C47E  49 8B D7                        mov rdx, r15
0062C481  49 8B CC                        mov rcx, r12
0062C484  E8 B7 11 0F 00                  call 0x14071d640
0062C489  48 85 F6                        test rsi, rsi
0062C48C  74 64                           je 0x14062c4f2
0062C48E  40 32 FF                        xor dil, dil
0062C491  40 38 3D 20 84 8D 00            cmp byte ptr [rip + 0x8d8420], dil
0062C498  75 0C                           jne 0x14062c4a6
0062C49A  F7 05 DC 84 8D 00 00 08 00 00   test dword ptr [rip + 0x8d84dc], 0x800
0062C4A4  74 13                           je 0x14062c4b9
0062C4A6  48 8D 0D D3 79 8D 00            lea rcx, [rip + 0x8d79d3]
0062C4AD  E8 6E A1 BE FF                  call 0x140216620
0062C4B2  40 8A F8                        mov dil, al
0062C4B5  84 C0                           test al, al
0062C4B7  74 39                           je 0x14062c4f2
0062C4B9  48 83 C6 30                     add rsi, 0x30
0062C4BD  48 8B 1E                        mov rbx, qword ptr [rsi]
0062C4C0  EB 1A                           jmp 0x14062c4dc
0062C4C2  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062C4C6  48 85 C0                        test rax, rax
0062C4C9  74 0E                           je 0x14062c4d9
0062C4CB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062C4CF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062C4D4  E8 F7 E5 08 00                  call 0x1406baad0
0062C4D9  48 8B 1B                        mov rbx, qword ptr [rbx]
0062C4DC  48 3B DE                        cmp rbx, rsi
0062C4DF  75 E1                           jne 0x14062c4c2
0062C4E1  40 84 FF                        test dil, dil
0062C4E4  74 0C                           je 0x14062c4f2
0062C4E6  48 8D 0D 93 79 8D 00            lea rcx, [rip + 0x8d7993]
0062C4ED  E8 8E D9 D1 FF                  call 0x140349e80
0062C4F2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062C4F7  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062C4FC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062C501  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0062C506  48 83 C4 40                     add rsp, 0x40
0062C50A  41 5F                           pop r15
0062C50C  41 5E                           pop r14
0062C50E  41 5C                           pop r12
0062C510  C3                              ret
0062C511  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoRegisterDriverReinitializationWrapper(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(319, a2, a3, a4);
    if (result == 0) goto loc_0062C47B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062C3FA;
    v_stack_m38 = v_stack_p0;
    goto loc_0062C408;
loc_0062C3FA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = a2;
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9274529)) != 0) goto loc_0062C42F;
    if (((*(unsigned int *)(v_rip + 9274707)) & (0x800ULL)) == 0) goto loc_0062C442;
loc_0062C42F:
    result = ExAcquireRundownProtection(v_rip + 9271882, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C47B;
loc_0062C442:
    goto loc_0062C465;
loc_0062C44B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C465:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062C44B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9271818;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoRegisterDriverReinitialization(a1, a2, a3, a4);
    if (result == 0) goto loc_0062C4F2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9274400)) != 0) goto loc_0062C4A6;
    if (((*(unsigned int *)(v_rip + 9274588)) & (0x800ULL)) == 0) goto loc_0062C4B9;
loc_0062C4A6:
    result = ExAcquireRundownProtection(v_rip + 9271763, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062C4F2;
loc_0062C4B9:
    v_rsi = (result) + (48);
    goto loc_0062C4DC;
loc_0062C4C2:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062C4DC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062C4C2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9271699;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoRegisterDriverReinitializationWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(319, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062C47B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062C3FA;
    v_stack_m38 = v_stack_p0;
    goto loc_0062C408;
loc_0062C3FA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8D84A1)) != 0) goto loc_0062C42F;
    if (((*(uint32_t *)(v_rip + 0x8D8553)) & (0x800ULL)) == 0) goto loc_0062C442;
loc_0062C42F:
    result = ExAcquireRundownProtection(v_rip + 9271882, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062C47B;
loc_0062C442:
    goto loc_0062C465;
loc_0062C44B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062C465:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062C44B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9271818;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = IoRegisterDriverReinitialization(Arg1, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062C4F2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D8420)) != 0) goto loc_0062C4A6;
    if (((*(uint32_t *)(v_rip + 0x8D84DC)) & (0x800ULL)) == 0) goto loc_0062C4B9;
loc_0062C4A6:
    result = ExAcquireRundownProtection(v_rip + 9271763, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062C4F2;
loc_0062C4B9:
    local_rsi = (result) + (48);
    goto loc_0062C4DC;
loc_0062C4C2:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0062C4DC:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062C4C2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9271699;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062C3A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062C3A0[BB_0062C3A0]
  bb_0062C3E7[BB_0062C3E7]
  bb_0062C3EE[BB_0062C3EE]
  bb_0062C3FA[BB_0062C3FA]
  bb_0062C3FE[BB_0062C3FE]
  bb_0062C408[BB_0062C408]
  bb_0062C423[BB_0062C423]
  bb_0062C42F[BB_0062C42F]
  bb_0062C442[BB_0062C442]
  bb_0062C44B[BB_0062C44B]
  bb_0062C454[BB_0062C454]
  bb_0062C462[BB_0062C462]
  bb_0062C465[BB_0062C465]
  bb_0062C46A[BB_0062C46A]
  bb_0062C46F[BB_0062C46F]
  bb_0062C47B[BB_0062C47B]
  bb_0062C48E[BB_0062C48E]
  bb_0062C49A[BB_0062C49A]
  bb_0062C4A6[BB_0062C4A6]
  bb_0062C4B9[BB_0062C4B9]
  bb_0062C4C2[BB_0062C4C2]
  bb_0062C4CB[BB_0062C4CB]
  bb_0062C4D9[BB_0062C4D9]
  bb_0062C4DC[BB_0062C4DC]
  bb_0062C4E1[BB_0062C4E1]
  bb_0062C4E6[BB_0062C4E6]
  bb_0062C4F2[BB_0062C4F2]
  bb_0062C511[BB_0062C511]
  bb_0062C3A0 -->|branch| bb_0062C47B
  bb_0062C3A0 -->|fallthrough| bb_0062C3E7
  bb_0062C3E7 -->|branch| bb_0062C3FA
  bb_0062C3E7 -->|fallthrough| bb_0062C3EE
  bb_0062C3EE -->|branch| bb_0062C408
  bb_0062C3FA -->|branch| bb_0062C408
  bb_0062C3FA -->|fallthrough| bb_0062C3FE
  bb_0062C3FE -->|flow| bb_0062C408
  bb_0062C408 -->|branch| bb_0062C42F
  bb_0062C408 -->|fallthrough| bb_0062C423
  bb_0062C423 -->|branch| bb_0062C442
  bb_0062C423 -->|fallthrough| bb_0062C42F
  bb_0062C42F -->|branch| bb_0062C47B
  bb_0062C42F -->|fallthrough| bb_0062C442
  bb_0062C442 -->|branch| bb_0062C465
  bb_0062C44B -->|branch| bb_0062C462
  bb_0062C44B -->|fallthrough| bb_0062C454
  bb_0062C454 -->|flow| bb_0062C462
  bb_0062C462 -->|flow| bb_0062C465
  bb_0062C465 -->|branch| bb_0062C44B
  bb_0062C465 -->|fallthrough| bb_0062C46A
  bb_0062C46A -->|branch| bb_0062C47B
  bb_0062C46A -->|fallthrough| bb_0062C46F
  bb_0062C46F -->|flow| bb_0062C47B
  bb_0062C47B -->|branch| bb_0062C4F2
  bb_0062C47B -->|fallthrough| bb_0062C48E
  bb_0062C48E -->|branch| bb_0062C4A6
  bb_0062C48E -->|fallthrough| bb_0062C49A
  bb_0062C49A -->|branch| bb_0062C4B9
  bb_0062C49A -->|fallthrough| bb_0062C4A6
  bb_0062C4A6 -->|branch| bb_0062C4F2
  bb_0062C4A6 -->|fallthrough| bb_0062C4B9
  bb_0062C4B9 -->|branch| bb_0062C4DC
  bb_0062C4C2 -->|branch| bb_0062C4D9
  bb_0062C4C2 -->|fallthrough| bb_0062C4CB
  bb_0062C4CB -->|flow| bb_0062C4D9
  bb_0062C4D9 -->|flow| bb_0062C4DC
  bb_0062C4DC -->|branch| bb_0062C4C2
  bb_0062C4DC -->|fallthrough| bb_0062C4E1
  bb_0062C4E1 -->|branch| bb_0062C4F2
  bb_0062C4E1 -->|fallthrough| bb_0062C4E6
  bb_0062C4E6 -->|flow| bb_0062C4F2
```
