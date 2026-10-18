# DifExAcquireFastMutexWrapper

- RVA: `0x0061D600`–`0x0061D750` (길이 `336` bytes)
- VA: `0x000000014061D600`
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
- `0x0061D628` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061D650` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061D67E` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D6A5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D6BE` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061D6C6` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x0061D6EF` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D716` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D72F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061D662` → RVA `0x00F048B8` (`.data`; read)
- `0x0061D66B` → RVA `0x00F04980` (`.data`; read)
- `0x0061D677` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061D600  48 8B C4                        mov rax, rsp
0061D603  48 89 58 08                     mov qword ptr [rax + 8], rbx
0061D607  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0061D60B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061D60F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061D613  41 56                           push r14
0061D615  48 83 EC 30                     sub rsp, 0x30
0061D619  48 8B E9                        mov rbp, rcx
0061D61C  0F 57 C0                        xorps xmm0, xmm0
0061D61F  B9 A9 01 00 00                  mov ecx, 0x1a9
0061D624  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
0061D628  E8 07 84 E7 FF                  call 0x140495a34
0061D62D  48 8B F8                        mov rdi, rax
0061D630  48 85 C0                        test rax, rax
0061D633  0F 84 8A 00 00 00               je 0x14061d6c3
0061D639  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061D63C  A8 18                           test al, 0x18
0061D63E  74 0C                           je 0x14061d64c
0061D640  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0061D645  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061D64A  EB 0E                           jmp 0x14061d65a
0061D64C  A8 04                           test al, 4
0061D64E  74 0A                           je 0x14061d65a
0061D650  E8 B3 65 EB FF                  call 0x1404d3c08
0061D655  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061D65A  40 32 F6                        xor sil, sil
0061D65D  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0061D662  40 38 35 4F 72 8E 00            cmp byte ptr [rip + 0x8e724f], sil
0061D669  75 0C                           jne 0x14061d677
0061D66B  F7 05 0B 73 8E 00 00 08 00 00   test dword ptr [rip + 0x8e730b], 0x800
0061D675  74 13                           je 0x14061d68a
0061D677  48 8D 0D 02 68 8E 00            lea rcx, [rip + 0x8e6802]
0061D67E  E8 9D 8F BF FF                  call 0x140216620
0061D683  40 8A F0                        mov sil, al
0061D686  84 C0                           test al, al
0061D688  74 39                           je 0x14061d6c3
0061D68A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0061D68E  49 8B 1E                        mov rbx, qword ptr [r14]
0061D691  EB 1A                           jmp 0x14061d6ad
0061D693  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D697  48 85 C0                        test rax, rax
0061D69A  74 0E                           je 0x14061d6aa
0061D69C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D6A0  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061D6A5  E8 26 D4 09 00                  call 0x1406baad0
0061D6AA  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D6AD  49 3B DE                        cmp rbx, r14
0061D6B0  75 E1                           jne 0x14061d693
0061D6B2  40 84 F6                        test sil, sil
0061D6B5  74 0C                           je 0x14061d6c3
0061D6B7  48 8D 0D C2 67 8E 00            lea rcx, [rip + 0x8e67c2]
0061D6BE  E8 BD C7 D2 FF                  call 0x140349e80
0061D6C3  48 8B CD                        mov rcx, rbp
0061D6C6  E8 D5 0E BF FF                  call 0x14020e5a0
0061D6CB  48 85 FF                        test rdi, rdi
0061D6CE  74 64                           je 0x14061d734
0061D6D0  40 32 F6                        xor sil, sil
0061D6D3  40 38 35 DE 71 8E 00            cmp byte ptr [rip + 0x8e71de], sil
0061D6DA  75 0C                           jne 0x14061d6e8
0061D6DC  F7 05 9A 72 8E 00 00 08 00 00   test dword ptr [rip + 0x8e729a], 0x800
0061D6E6  74 13                           je 0x14061d6fb
0061D6E8  48 8D 0D 91 67 8E 00            lea rcx, [rip + 0x8e6791]
0061D6EF  E8 2C 8F BF FF                  call 0x140216620
0061D6F4  40 8A F0                        mov sil, al
0061D6F7  84 C0                           test al, al
0061D6F9  74 39                           je 0x14061d734
0061D6FB  48 83 C7 30                     add rdi, 0x30
0061D6FF  48 8B 1F                        mov rbx, qword ptr [rdi]
0061D702  EB 1A                           jmp 0x14061d71e
0061D704  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D708  48 85 C0                        test rax, rax
0061D70B  74 0E                           je 0x14061d71b
0061D70D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D711  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061D716  E8 B5 D3 09 00                  call 0x1406baad0
0061D71B  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D71E  48 3B DF                        cmp rbx, rdi
0061D721  75 E1                           jne 0x14061d704
0061D723  40 84 F6                        test sil, sil
0061D726  74 0C                           je 0x14061d734
0061D728  48 8D 0D 51 67 8E 00            lea rcx, [rip + 0x8e6751]
0061D72F  E8 4C C7 D2 FF                  call 0x140349e80
0061D734  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0061D739  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
0061D73E  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0061D743  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0061D748  48 83 C4 30                     add rsp, 0x30
0061D74C  41 5E                           pop r14
0061D74E  C3                              ret
0061D74F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExAcquireFastMutexWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(425, a2, a3, a4);
    if (result == 0) goto loc_0061D6C3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061D64C;
    v_stack_m18 = v_stack_p0;
    goto loc_0061D65A;
loc_0061D64C:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9335375)) != 0) goto loc_0061D677;
    if (((*(unsigned int *)(v_rip + 9335563)) & (0x800ULL)) == 0) goto loc_0061D68A;
loc_0061D677:
    result = ExAcquireRundownProtection(v_rip + 9332738, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D6C3;
loc_0061D68A:
    goto loc_0061D6AD;
loc_0061D693:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D6AD:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061D693;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9332674;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExAcquireFastMutex(a1, a2, a3, a4);
    if (result == 0) goto loc_0061D734;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9335262)) != 0) goto loc_0061D6E8;
    if (((*(unsigned int *)(v_rip + 9335450)) & (0x800ULL)) == 0) goto loc_0061D6FB;
loc_0061D6E8:
    result = ExAcquireRundownProtection(v_rip + 9332625, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D734;
loc_0061D6FB:
    v_rdi = (result) + (48);
    goto loc_0061D71E;
loc_0061D704:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D71E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_0061D704;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9332561;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExAcquireFastMutexWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(425, a2, a3, a4);
    if (result == 0) goto loc_0061D6C3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061D64C;
    v_stack_m18 = v_stack_p0;
    goto loc_0061D65A;
loc_0061D64C:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E724F)) != 0) goto loc_0061D677;
    if (((*(uint32_t *)(v_rip + 0x8E730B)) & (0x800ULL)) == 0) goto loc_0061D68A;
loc_0061D677:
    result = ExAcquireRundownProtection(v_rip + 9332738, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D6C3;
loc_0061D68A:
    goto loc_0061D6AD;
loc_0061D693:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061D6AD:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061D693;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9332674;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExAcquireFastMutex(Arg1, a2, a3, a4);
    if (result == 0) goto loc_0061D734;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E71DE)) != 0) goto loc_0061D6E8;
    if (((*(uint32_t *)(v_rip + 0x8E729A)) & (0x800ULL)) == 0) goto loc_0061D6FB;
loc_0061D6E8:
    result = ExAcquireRundownProtection(v_rip + 9332625, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D734;
loc_0061D6FB:
    local_rdi = (result) + (48);
    goto loc_0061D71E;
loc_0061D704:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061D71E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_0061D704;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9332561;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061D600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061D600[BB_0061D600]
  bb_0061D639[BB_0061D639]
  bb_0061D640[BB_0061D640]
  bb_0061D64C[BB_0061D64C]
  bb_0061D650[BB_0061D650]
  bb_0061D65A[BB_0061D65A]
  bb_0061D66B[BB_0061D66B]
  bb_0061D677[BB_0061D677]
  bb_0061D68A[BB_0061D68A]
  bb_0061D693[BB_0061D693]
  bb_0061D69C[BB_0061D69C]
  bb_0061D6AA[BB_0061D6AA]
  bb_0061D6AD[BB_0061D6AD]
  bb_0061D6B2[BB_0061D6B2]
  bb_0061D6B7[BB_0061D6B7]
  bb_0061D6C3[BB_0061D6C3]
  bb_0061D6D0[BB_0061D6D0]
  bb_0061D6DC[BB_0061D6DC]
  bb_0061D6E8[BB_0061D6E8]
  bb_0061D6FB[BB_0061D6FB]
  bb_0061D704[BB_0061D704]
  bb_0061D70D[BB_0061D70D]
  bb_0061D71B[BB_0061D71B]
  bb_0061D71E[BB_0061D71E]
  bb_0061D723[BB_0061D723]
  bb_0061D728[BB_0061D728]
  bb_0061D734[BB_0061D734]
  bb_0061D74F[BB_0061D74F]
  bb_0061D600 -->|branch| bb_0061D6C3
  bb_0061D600 -->|fallthrough| bb_0061D639
  bb_0061D639 -->|branch| bb_0061D64C
  bb_0061D639 -->|fallthrough| bb_0061D640
  bb_0061D640 -->|branch| bb_0061D65A
  bb_0061D64C -->|branch| bb_0061D65A
  bb_0061D64C -->|fallthrough| bb_0061D650
  bb_0061D650 -->|flow| bb_0061D65A
  bb_0061D65A -->|branch| bb_0061D677
  bb_0061D65A -->|fallthrough| bb_0061D66B
  bb_0061D66B -->|branch| bb_0061D68A
  bb_0061D66B -->|fallthrough| bb_0061D677
  bb_0061D677 -->|branch| bb_0061D6C3
  bb_0061D677 -->|fallthrough| bb_0061D68A
  bb_0061D68A -->|branch| bb_0061D6AD
  bb_0061D693 -->|branch| bb_0061D6AA
  bb_0061D693 -->|fallthrough| bb_0061D69C
  bb_0061D69C -->|flow| bb_0061D6AA
  bb_0061D6AA -->|flow| bb_0061D6AD
  bb_0061D6AD -->|branch| bb_0061D693
  bb_0061D6AD -->|fallthrough| bb_0061D6B2
  bb_0061D6B2 -->|branch| bb_0061D6C3
  bb_0061D6B2 -->|fallthrough| bb_0061D6B7
  bb_0061D6B7 -->|flow| bb_0061D6C3
  bb_0061D6C3 -->|branch| bb_0061D734
  bb_0061D6C3 -->|fallthrough| bb_0061D6D0
  bb_0061D6D0 -->|branch| bb_0061D6E8
  bb_0061D6D0 -->|fallthrough| bb_0061D6DC
  bb_0061D6DC -->|branch| bb_0061D6FB
  bb_0061D6DC -->|fallthrough| bb_0061D6E8
  bb_0061D6E8 -->|branch| bb_0061D734
  bb_0061D6E8 -->|fallthrough| bb_0061D6FB
  bb_0061D6FB -->|branch| bb_0061D71E
  bb_0061D704 -->|branch| bb_0061D71B
  bb_0061D704 -->|fallthrough| bb_0061D70D
  bb_0061D70D -->|flow| bb_0061D71B
  bb_0061D71B -->|flow| bb_0061D71E
  bb_0061D71E -->|branch| bb_0061D704
  bb_0061D71E -->|fallthrough| bb_0061D723
  bb_0061D723 -->|branch| bb_0061D734
  bb_0061D723 -->|fallthrough| bb_0061D728
  bb_0061D728 -->|flow| bb_0061D734
```
