# DifExAcquireFastMutexUnsafeWrapper

- RVA: `0x0061D4A0`–`0x0061D5F0` (길이 `336` bytes)
- VA: `0x000000014061D4A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `90`개 명령, `336/336` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061D4C8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061D4F0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061D51E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D545` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D55E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061D566` → [ExAcquireFastMutexUnsafe](../3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x0061D58F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D5B6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D5CF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061D502` → RVA `0x00F048B8` (`.data`; read)
- `0x0061D50B` → RVA `0x00F04980` (`.data`; read)
- `0x0061D517` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061D4A0  48 8B C4                        mov rax, rsp
0061D4A3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0061D4A7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0061D4AB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061D4AF  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061D4B3  41 56                           push r14
0061D4B5  48 83 EC 30                     sub rsp, 0x30
0061D4B9  48 8B E9                        mov rbp, rcx
0061D4BC  0F 57 C0                        xorps xmm0, xmm0
0061D4BF  B9 A8 01 00 00                  mov ecx, 0x1a8
0061D4C4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0061D4C8  E8 67 85 E7 FF                  call 0x140495a34
0061D4CD  48 8B F8                        mov rdi, rax
0061D4D0  48 85 C0                        test rax, rax
0061D4D3  0F 84 8A 00 00 00               je 0x14061d563
0061D4D9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061D4DC  A8 18                           test al, 0x18
0061D4DE  74 0C                           je 0x14061d4ec
0061D4E0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0061D4E5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061D4EA  EB 0E                           jmp 0x14061d4fa
0061D4EC  A8 04                           test al, 4
0061D4EE  74 0A                           je 0x14061d4fa
0061D4F0  E8 13 67 EB FF                  call 0x1404d3c08
0061D4F5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061D4FA  40 32 F6                        xor sil, sil
0061D4FD  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061D502  40 38 35 AF 73 8E 00            cmp byte ptr [rip + 0x8e73af], sil
0061D509  75 0C                           jne 0x14061d517
0061D50B  F7 05 6B 74 8E 00 00 08 00 00   test dword ptr [rip + 0x8e746b], 0x800
0061D515  74 13                           je 0x14061d52a
0061D517  48 8D 0D 62 69 8E 00            lea rcx, [rip + 0x8e6962]
0061D51E  E8 FD 90 BF FF                  call 0x140216620
0061D523  40 8A F0                        mov sil, al
0061D526  84 C0                           test al, al
0061D528  74 39                           je 0x14061d563
0061D52A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0061D52E  49 8B 1E                        mov rbx, qword ptr [r14]
0061D531  EB 1A                           jmp 0x14061d54d
0061D533  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D537  48 85 C0                        test rax, rax
0061D53A  74 0E                           je 0x14061d54a
0061D53C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D540  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061D545  E8 86 D5 09 00                  call 0x1406baad0
0061D54A  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D54D  49 3B DE                        cmp rbx, r14
0061D550  75 E1                           jne 0x14061d533
0061D552  40 84 F6                        test sil, sil
0061D555  74 0C                           je 0x14061d563
0061D557  48 8D 0D 22 69 8E 00            lea rcx, [rip + 0x8e6922]
0061D55E  E8 1D C9 D2 FF                  call 0x140349e80
0061D563  48 8B CD                        mov rcx, rbp
0061D566  E8 B5 61 DD FF                  call 0x1403f3720
0061D56B  48 85 FF                        test rdi, rdi
0061D56E  74 64                           je 0x14061d5d4
0061D570  40 32 F6                        xor sil, sil
0061D573  40 38 35 3E 73 8E 00            cmp byte ptr [rip + 0x8e733e], sil
0061D57A  75 0C                           jne 0x14061d588
0061D57C  F7 05 FA 73 8E 00 00 08 00 00   test dword ptr [rip + 0x8e73fa], 0x800
0061D586  74 13                           je 0x14061d59b
0061D588  48 8D 0D F1 68 8E 00            lea rcx, [rip + 0x8e68f1]
0061D58F  E8 8C 90 BF FF                  call 0x140216620
0061D594  40 8A F0                        mov sil, al
0061D597  84 C0                           test al, al
0061D599  74 39                           je 0x14061d5d4
0061D59B  48 83 C7 30                     add rdi, 0x30
0061D59F  48 8B 1F                        mov rbx, qword ptr [rdi]
0061D5A2  EB 1A                           jmp 0x14061d5be
0061D5A4  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D5A8  48 85 C0                        test rax, rax
0061D5AB  74 0E                           je 0x14061d5bb
0061D5AD  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D5B1  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061D5B6  E8 15 D5 09 00                  call 0x1406baad0
0061D5BB  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D5BE  48 3B DF                        cmp rbx, rdi
0061D5C1  75 E1                           jne 0x14061d5a4
0061D5C3  40 84 F6                        test sil, sil
0061D5C6  74 0C                           je 0x14061d5d4
0061D5C8  48 8D 0D B1 68 8E 00            lea rcx, [rip + 0x8e68b1]
0061D5CF  E8 AC C8 D2 FF                  call 0x140349e80
0061D5D4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0061D5D9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0061D5DE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0061D5E3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0061D5E8  48 83 C4 30                     add rsp, 0x30
0061D5EC  41 5E                           pop r14
0061D5EE  C3                              ret
0061D5EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExAcquireFastMutexUnsafeWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    result = DifGetAPIThunkContextById(424, a2, a3, a4);
    if (result == 0) goto loc_0061D563;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061D4EC;
    v_stack_m18 = v_stack_p0;
    goto loc_0061D4FA;
loc_0061D4EC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9335727)) != 0) goto loc_0061D517;
    if (((*(unsigned int *)(v_rip + 9335915)) & (0x800ULL)) == 0) goto loc_0061D52A;
loc_0061D517:
    result = ExAcquireRundownProtection(v_rip + 9333090, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D563;
loc_0061D52A:
    goto loc_0061D54D;
loc_0061D533:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D54D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061D533;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9333026;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExAcquireFastMutexUnsafe(a1, a2, a3, a4);
    if (result == 0) goto loc_0061D5D4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9335614)) != 0) goto loc_0061D588;
    if (((*(unsigned int *)(v_rip + 9335802)) & (0x800ULL)) == 0) goto loc_0061D59B;
loc_0061D588:
    result = ExAcquireRundownProtection(v_rip + 9332977, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D5D4;
loc_0061D59B:
    v_rdi = (result) + (48);
    goto loc_0061D5BE;
loc_0061D5A4:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D5BE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0061D5A4;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9332913;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExAcquireFastMutexUnsafeWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    result = DifGetAPIThunkContextById(424, a2, a3, a4);
    if (result == 0) goto loc_0061D563;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061D4EC;
    v_stack_m18 = v_stack_p0;
    goto loc_0061D4FA;
loc_0061D4EC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E73AF)) != 0) goto loc_0061D517;
    if (((*(uint32_t *)(v_rip + 0x8E746B)) & (0x800ULL)) == 0) goto loc_0061D52A;
loc_0061D517:
    result = ExAcquireRundownProtection(v_rip + 9333090, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D563;
loc_0061D52A:
    goto loc_0061D54D;
loc_0061D533:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061D54D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061D533;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9333026;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExAcquireFastMutexUnsafe(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0061D5D4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E733E)) != 0) goto loc_0061D588;
    if (((*(uint32_t *)(v_rip + 0x8E73FA)) & (0x800ULL)) == 0) goto loc_0061D59B;
loc_0061D588:
    result = ExAcquireRundownProtection(v_rip + 9332977, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D5D4;
loc_0061D59B:
    local_rdi = (result) + (48);
    goto loc_0061D5BE;
loc_0061D5A4:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061D5BE:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0061D5A4;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9332913;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061D4A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061D4A0[BB_0061D4A0]
  bb_0061D4D9[BB_0061D4D9]
  bb_0061D4E0[BB_0061D4E0]
  bb_0061D4EC[BB_0061D4EC]
  bb_0061D4F0[BB_0061D4F0]
  bb_0061D4FA[BB_0061D4FA]
  bb_0061D50B[BB_0061D50B]
  bb_0061D517[BB_0061D517]
  bb_0061D52A[BB_0061D52A]
  bb_0061D533[BB_0061D533]
  bb_0061D53C[BB_0061D53C]
  bb_0061D54A[BB_0061D54A]
  bb_0061D54D[BB_0061D54D]
  bb_0061D552[BB_0061D552]
  bb_0061D557[BB_0061D557]
  bb_0061D563[BB_0061D563]
  bb_0061D570[BB_0061D570]
  bb_0061D57C[BB_0061D57C]
  bb_0061D588[BB_0061D588]
  bb_0061D59B[BB_0061D59B]
  bb_0061D5A4[BB_0061D5A4]
  bb_0061D5AD[BB_0061D5AD]
  bb_0061D5BB[BB_0061D5BB]
  bb_0061D5BE[BB_0061D5BE]
  bb_0061D5C3[BB_0061D5C3]
  bb_0061D5C8[BB_0061D5C8]
  bb_0061D5D4[BB_0061D5D4]
  bb_0061D5EF[BB_0061D5EF]
  bb_0061D4A0 -->|branch| bb_0061D563
  bb_0061D4A0 -->|fallthrough| bb_0061D4D9
  bb_0061D4D9 -->|branch| bb_0061D4EC
  bb_0061D4D9 -->|fallthrough| bb_0061D4E0
  bb_0061D4E0 -->|branch| bb_0061D4FA
  bb_0061D4EC -->|branch| bb_0061D4FA
  bb_0061D4EC -->|fallthrough| bb_0061D4F0
  bb_0061D4F0 -->|flow| bb_0061D4FA
  bb_0061D4FA -->|branch| bb_0061D517
  bb_0061D4FA -->|fallthrough| bb_0061D50B
  bb_0061D50B -->|branch| bb_0061D52A
  bb_0061D50B -->|fallthrough| bb_0061D517
  bb_0061D517 -->|branch| bb_0061D563
  bb_0061D517 -->|fallthrough| bb_0061D52A
  bb_0061D52A -->|branch| bb_0061D54D
  bb_0061D533 -->|branch| bb_0061D54A
  bb_0061D533 -->|fallthrough| bb_0061D53C
  bb_0061D53C -->|flow| bb_0061D54A
  bb_0061D54A -->|flow| bb_0061D54D
  bb_0061D54D -->|branch| bb_0061D533
  bb_0061D54D -->|fallthrough| bb_0061D552
  bb_0061D552 -->|branch| bb_0061D563
  bb_0061D552 -->|fallthrough| bb_0061D557
  bb_0061D557 -->|flow| bb_0061D563
  bb_0061D563 -->|branch| bb_0061D5D4
  bb_0061D563 -->|fallthrough| bb_0061D570
  bb_0061D570 -->|branch| bb_0061D588
  bb_0061D570 -->|fallthrough| bb_0061D57C
  bb_0061D57C -->|branch| bb_0061D59B
  bb_0061D57C -->|fallthrough| bb_0061D588
  bb_0061D588 -->|branch| bb_0061D5D4
  bb_0061D588 -->|fallthrough| bb_0061D59B
  bb_0061D59B -->|branch| bb_0061D5BE
  bb_0061D5A4 -->|branch| bb_0061D5BB
  bb_0061D5A4 -->|fallthrough| bb_0061D5AD
  bb_0061D5AD -->|flow| bb_0061D5BB
  bb_0061D5BB -->|flow| bb_0061D5BE
  bb_0061D5BE -->|branch| bb_0061D5A4
  bb_0061D5BE -->|fallthrough| bb_0061D5C3
  bb_0061D5C3 -->|branch| bb_0061D5D4
  bb_0061D5C3 -->|fallthrough| bb_0061D5C8
  bb_0061D5C8 -->|flow| bb_0061D5D4
```
