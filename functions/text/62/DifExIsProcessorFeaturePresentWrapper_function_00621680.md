# DifExIsProcessorFeaturePresentWrapper

- RVA: `0x00621680`–`0x006217D5` (길이 `341` bytes)
- VA: `0x0000000140621680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `92`개 명령, `341/341` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006216A7` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006216CF` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006216FC` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621723` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062173C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00621743` → [RtlIsProcessorFeaturePresent](../4B/RtlIsProcessorFeaturePresent_function_004B22C0.md) (function, `0x004B22C0`)
- `0x00621770` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621797` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006217B0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006216E0` → RVA `0x00F048B8` (`.data`; read)
- `0x006216E9` → RVA `0x00F04980` (`.data`; read)
- `0x006216F5` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00621680  48 8B C4                        mov rax, rsp
00621683  48 89 58 08                     mov qword ptr [rax + 8], rbx
00621687  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062168B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062168F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00621693  41 56                           push r14
00621695  48 83 EC 30                     sub rsp, 0x30
00621699  8B E9                           mov ebp, ecx
0062169B  0F 57 C0                        xorps xmm0, xmm0
0062169E  B9 8B 01 00 00                  mov ecx, 0x18b
006216A3  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
006216A7  E8 88 43 E7 FF                  call 0x140495a34
006216AC  48 8B F0                        mov rsi, rax
006216AF  48 85 C0                        test rax, rax
006216B2  0F 84 89 00 00 00               je 0x140621741
006216B8  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006216BB  A8 18                           test al, 0x18
006216BD  74 0C                           je 0x1406216cb
006216BF  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
006216C4  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006216C9  EB 0E                           jmp 0x1406216d9
006216CB  A8 04                           test al, 4
006216CD  74 0A                           je 0x1406216d9
006216CF  E8 34 25 EB FF                  call 0x1404d3c08
006216D4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006216D9  40 32 FF                        xor dil, dil
006216DC  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
006216E0  40 38 3D D1 31 8E 00            cmp byte ptr [rip + 0x8e31d1], dil
006216E7  75 0C                           jne 0x1406216f5
006216E9  F7 05 8D 32 8E 00 00 08 00 00   test dword ptr [rip + 0x8e328d], 0x800
006216F3  74 13                           je 0x140621708
006216F5  48 8D 0D 84 27 8E 00            lea rcx, [rip + 0x8e2784]
006216FC  E8 1F 4F BF FF                  call 0x140216620
00621701  40 8A F8                        mov dil, al
00621704  84 C0                           test al, al
00621706  74 39                           je 0x140621741
00621708  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062170C  49 8B 1E                        mov rbx, qword ptr [r14]
0062170F  EB 1A                           jmp 0x14062172b
00621711  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621715  48 85 C0                        test rax, rax
00621718  74 0E                           je 0x140621728
0062171A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062171E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00621723  E8 A8 93 09 00                  call 0x1406baad0
00621728  48 8B 1B                        mov rbx, qword ptr [rbx]
0062172B  49 3B DE                        cmp rbx, r14
0062172E  75 E1                           jne 0x140621711
00621730  40 84 FF                        test dil, dil
00621733  74 0C                           je 0x140621741
00621735  48 8D 0D 44 27 8E 00            lea rcx, [rip + 0x8e2744]
0062173C  E8 3F 87 D2 FF                  call 0x140349e80
00621741  8B CD                           mov ecx, ebp
00621743  E8 78 0B E9 FF                  call 0x1404b22c0
00621748  88 44 24 2C                     mov byte ptr [rsp + 0x2c], al
0062174C  48 85 F6                        test rsi, rsi
0062174F  74 64                           je 0x1406217b5
00621751  40 32 FF                        xor dil, dil
00621754  40 38 3D 5D 31 8E 00            cmp byte ptr [rip + 0x8e315d], dil
0062175B  75 0C                           jne 0x140621769
0062175D  F7 05 19 32 8E 00 00 08 00 00   test dword ptr [rip + 0x8e3219], 0x800
00621767  74 13                           je 0x14062177c
00621769  48 8D 0D 10 27 8E 00            lea rcx, [rip + 0x8e2710]
00621770  E8 AB 4E BF FF                  call 0x140216620
00621775  40 8A F8                        mov dil, al
00621778  84 C0                           test al, al
0062177A  74 39                           je 0x1406217b5
0062177C  48 83 C6 30                     add rsi, 0x30
00621780  48 8B 1E                        mov rbx, qword ptr [rsi]
00621783  EB 1A                           jmp 0x14062179f
00621785  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621789  48 85 C0                        test rax, rax
0062178C  74 0E                           je 0x14062179c
0062178E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621792  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00621797  E8 34 93 09 00                  call 0x1406baad0
0062179C  48 8B 1B                        mov rbx, qword ptr [rbx]
0062179F  48 3B DE                        cmp rbx, rsi
006217A2  75 E1                           jne 0x140621785
006217A4  40 84 FF                        test dil, dil
006217A7  74 0C                           je 0x1406217b5
006217A9  48 8D 0D D0 26 8E 00            lea rcx, [rip + 0x8e26d0]
006217B0  E8 CB 86 D2 FF                  call 0x140349e80
006217B5  8A 44 24 2C                     mov al, byte ptr [rsp + 0x2c]
006217B9  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
006217BE  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
006217C3  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
006217C8  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
006217CD  48 83 C4 30                     add rsp, 0x30
006217D1  41 5E                           pop r14
006217D3  C3                              ret
006217D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExIsProcessorFeaturePresentWrapper(int a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int8 v_stack_mC;
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
    result = DifGetAPIThunkContextById(395, a2, a3, a4);
    if (result == 0) goto loc_00621741;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006216CB;
    v_stack_m18 = v_stack_p0;
    goto loc_006216D9;
loc_006216CB:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rdi = 0;
    v_stack_m10 = (unsigned int)((unsigned int)(a1));
    if ((*(unsigned __int8 *)(v_rip + 9318865)) != 0) goto loc_006216F5;
    if (((*(unsigned int *)(v_rip + 9319053)) & (0x800ULL)) == 0) goto loc_00621708;
loc_006216F5:
    result = ExAcquireRundownProtection(v_rip + 9316228, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00621741;
loc_00621708:
    goto loc_0062172B;
loc_00621711:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062172B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00621711;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9316164;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlIsProcessorFeaturePresent((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
    v_stack_mC = (unsigned __int8)(result);
    if (result == 0) goto loc_006217B5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9318749)) != 0) goto loc_00621769;
    if (((*(unsigned int *)(v_rip + 9318937)) & (0x800ULL)) == 0) goto loc_0062177C;
loc_00621769:
    result = ExAcquireRundownProtection(v_rip + 9316112, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006217B5;
loc_0062177C:
    v_rsi = (result) + (48);
    goto loc_0062179F;
loc_00621785:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062179F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00621785;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9316048;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return v_stack_mC;
}
```

## 5. (Beta) C Style

```c
int64_t DifExIsProcessorFeaturePresentWrapper(int32_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint8_t v_stack_mC;
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
    result = DifGetAPIThunkContextById(395, a2, a3, a4);
    if (result == 0) goto loc_00621741;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006216CB;
    v_stack_m18 = v_stack_p0;
    goto loc_006216D9;
loc_006216CB:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rdi = 0;
    v_stack_m10 = (uint32_t)((uint32_t)(Arg1));
    if ((*(uint8_t *)(v_rip + 0x8E31D1)) != 0) goto loc_006216F5;
    if (((*(uint32_t *)(v_rip + 0x8E328D)) & (0x800ULL)) == 0) goto loc_00621708;
loc_006216F5:
    result = ExAcquireRundownProtection(v_rip + 9316228, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00621741;
loc_00621708:
    goto loc_0062172B;
loc_00621711:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062172B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00621711;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9316164;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = RtlIsProcessorFeaturePresent((uint32_t)((uint32_t)((uint32_t)(Arg1))), a2, a3, a4);
    v_stack_mC = (uint8_t)(result);
    if (result == 0) goto loc_006217B5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E315D)) != 0) goto loc_00621769;
    if (((*(uint32_t *)(v_rip + 0x8E3219)) & (0x800ULL)) == 0) goto loc_0062177C;
loc_00621769:
    result = ExAcquireRundownProtection(v_rip + 9316112, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006217B5;
loc_0062177C:
    local_rsi = (result) + (48);
    goto loc_0062179F;
loc_00621785:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062179F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00621785;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9316048;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return v_stack_mC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00621680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00621680[BB_00621680]
  bb_006216B8[BB_006216B8]
  bb_006216BF[BB_006216BF]
  bb_006216CB[BB_006216CB]
  bb_006216CF[BB_006216CF]
  bb_006216D9[BB_006216D9]
  bb_006216E9[BB_006216E9]
  bb_006216F5[BB_006216F5]
  bb_00621708[BB_00621708]
  bb_00621711[BB_00621711]
  bb_0062171A[BB_0062171A]
  bb_00621728[BB_00621728]
  bb_0062172B[BB_0062172B]
  bb_00621730[BB_00621730]
  bb_00621735[BB_00621735]
  bb_00621741[BB_00621741]
  bb_00621751[BB_00621751]
  bb_0062175D[BB_0062175D]
  bb_00621769[BB_00621769]
  bb_0062177C[BB_0062177C]
  bb_00621785[BB_00621785]
  bb_0062178E[BB_0062178E]
  bb_0062179C[BB_0062179C]
  bb_0062179F[BB_0062179F]
  bb_006217A4[BB_006217A4]
  bb_006217A9[BB_006217A9]
  bb_006217B5[BB_006217B5]
  bb_006217D4[BB_006217D4]
  bb_00621680 -->|branch| bb_00621741
  bb_00621680 -->|fallthrough| bb_006216B8
  bb_006216B8 -->|branch| bb_006216CB
  bb_006216B8 -->|fallthrough| bb_006216BF
  bb_006216BF -->|branch| bb_006216D9
  bb_006216CB -->|branch| bb_006216D9
  bb_006216CB -->|fallthrough| bb_006216CF
  bb_006216CF -->|flow| bb_006216D9
  bb_006216D9 -->|branch| bb_006216F5
  bb_006216D9 -->|fallthrough| bb_006216E9
  bb_006216E9 -->|branch| bb_00621708
  bb_006216E9 -->|fallthrough| bb_006216F5
  bb_006216F5 -->|branch| bb_00621741
  bb_006216F5 -->|fallthrough| bb_00621708
  bb_00621708 -->|branch| bb_0062172B
  bb_00621711 -->|branch| bb_00621728
  bb_00621711 -->|fallthrough| bb_0062171A
  bb_0062171A -->|flow| bb_00621728
  bb_00621728 -->|flow| bb_0062172B
  bb_0062172B -->|branch| bb_00621711
  bb_0062172B -->|fallthrough| bb_00621730
  bb_00621730 -->|branch| bb_00621741
  bb_00621730 -->|fallthrough| bb_00621735
  bb_00621735 -->|flow| bb_00621741
  bb_00621741 -->|branch| bb_006217B5
  bb_00621741 -->|fallthrough| bb_00621751
  bb_00621751 -->|branch| bb_00621769
  bb_00621751 -->|fallthrough| bb_0062175D
  bb_0062175D -->|branch| bb_0062177C
  bb_0062175D -->|fallthrough| bb_00621769
  bb_00621769 -->|branch| bb_006217B5
  bb_00621769 -->|fallthrough| bb_0062177C
  bb_0062177C -->|branch| bb_0062179F
  bb_00621785 -->|branch| bb_0062179C
  bb_00621785 -->|fallthrough| bb_0062178E
  bb_0062178E -->|flow| bb_0062179C
  bb_0062179C -->|flow| bb_0062179F
  bb_0062179F -->|branch| bb_00621785
  bb_0062179F -->|fallthrough| bb_006217A4
  bb_006217A4 -->|branch| bb_006217B5
  bb_006217A4 -->|fallthrough| bb_006217A9
  bb_006217A9 -->|flow| bb_006217B5
```
