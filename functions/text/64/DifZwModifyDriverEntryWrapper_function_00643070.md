# DifZwModifyDriverEntryWrapper

- RVA: `0x00643070`–`0x006431CD` (길이 `349` bytes)
- VA: `0x0000000140643070`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `349/349` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064309D` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006430C5` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006430F3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064311A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00643133` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064313B` → [ZwModifyDriverEntry](../6A/ZwModifyDriverEntry_function_006AF4F0.md) (function, `0x006AF4F0`)
- `0x00643168` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064318F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006431A8` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006430D7` → RVA `0x00F048B8` (`.data`; read)
- `0x006430E0` → RVA `0x00F04980` (`.data`; read)
- `0x006430EC` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00643070  4C 8B DC                        mov r11, rsp
00643073  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00643077  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0064307B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0064307F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00643083  41 56                           push r14
00643085  48 83 EC 40                     sub rsp, 0x40
00643089  33 C0                           xor eax, eax
0064308B  0F 57 C0                        xorps xmm0, xmm0
0064308E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00643093  48 8B E9                        mov rbp, rcx
00643096  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0064309A  8D 48 5A                        lea ecx, [rax + 0x5a]
0064309D  E8 92 29 E5 FF                  call 0x140495a34
006430A2  48 8B F0                        mov rsi, rax
006430A5  48 85 C0                        test rax, rax
006430A8  0F 84 8A 00 00 00               je 0x140643138
006430AE  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006430B1  A8 18                           test al, 0x18
006430B3  74 0C                           je 0x1406430c1
006430B5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006430BA  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006430BF  EB 0E                           jmp 0x1406430cf
006430C1  A8 04                           test al, 4
006430C3  74 0A                           je 0x1406430cf
006430C5  E8 3E 0B E9 FF                  call 0x1404d3c08
006430CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006430CF  40 32 FF                        xor dil, dil
006430D2  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006430D7  40 38 3D DA 17 8C 00            cmp byte ptr [rip + 0x8c17da], dil
006430DE  75 0C                           jne 0x1406430ec
006430E0  F7 05 96 18 8C 00 00 08 00 00   test dword ptr [rip + 0x8c1896], 0x800
006430EA  74 13                           je 0x1406430ff
006430EC  48 8D 0D 8D 0D 8C 00            lea rcx, [rip + 0x8c0d8d]
006430F3  E8 28 35 BD FF                  call 0x140216620
006430F8  40 8A F8                        mov dil, al
006430FB  84 C0                           test al, al
006430FD  74 39                           je 0x140643138
006430FF  4C 8D 76 20                     lea r14, [rsi + 0x20]
00643103  49 8B 1E                        mov rbx, qword ptr [r14]
00643106  EB 1A                           jmp 0x140643122
00643108  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064310C  48 85 C0                        test rax, rax
0064310F  74 0E                           je 0x14064311f
00643111  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00643115  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064311A  E8 B1 79 07 00                  call 0x1406baad0
0064311F  48 8B 1B                        mov rbx, qword ptr [rbx]
00643122  49 3B DE                        cmp rbx, r14
00643125  75 E1                           jne 0x140643108
00643127  40 84 FF                        test dil, dil
0064312A  74 0C                           je 0x140643138
0064312C  48 8D 0D 4D 0D 8C 00            lea rcx, [rip + 0x8c0d4d]
00643133  E8 48 6D D0 FF                  call 0x140349e80
00643138  48 8B CD                        mov rcx, rbp
0064313B  E8 B0 C3 06 00                  call 0x1406af4f0
00643140  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00643144  48 85 F6                        test rsi, rsi
00643147  74 64                           je 0x1406431ad
00643149  40 32 FF                        xor dil, dil
0064314C  40 38 3D 65 17 8C 00            cmp byte ptr [rip + 0x8c1765], dil
00643153  75 0C                           jne 0x140643161
00643155  F7 05 21 18 8C 00 00 08 00 00   test dword ptr [rip + 0x8c1821], 0x800
0064315F  74 13                           je 0x140643174
00643161  48 8D 0D 18 0D 8C 00            lea rcx, [rip + 0x8c0d18]
00643168  E8 B3 34 BD FF                  call 0x140216620
0064316D  40 8A F8                        mov dil, al
00643170  84 C0                           test al, al
00643172  74 39                           je 0x1406431ad
00643174  48 83 C6 30                     add rsi, 0x30
00643178  48 8B 1E                        mov rbx, qword ptr [rsi]
0064317B  EB 1A                           jmp 0x140643197
0064317D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00643181  48 85 C0                        test rax, rax
00643184  74 0E                           je 0x140643194
00643186  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064318A  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064318F  E8 3C 79 07 00                  call 0x1406baad0
00643194  48 8B 1B                        mov rbx, qword ptr [rbx]
00643197  48 3B DE                        cmp rbx, rsi
0064319A  75 E1                           jne 0x14064317d
0064319C  40 84 FF                        test dil, dil
0064319F  74 0C                           je 0x1406431ad
006431A1  48 8D 0D D8 0C 8C 00            lea rcx, [rip + 0x8c0cd8]
006431A8  E8 D3 6C D0 FF                  call 0x140349e80
006431AD  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
006431B1  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006431B6  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006431BB  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006431C0  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006431C5  48 83 C4 40                     add rsp, 0x40
006431C9  41 5E                           pop r14
006431CB  C3                              ret
006431CC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwModifyDriverEntryWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
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
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(result + 90, a2, a3, a4);
    if (result == 0) goto loc_00643138;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006430C1;
    v_stack_m28 = v_stack_p0;
    goto loc_006430CF;
loc_006430C1:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9181146)) != 0) goto loc_006430EC;
    if (((*(unsigned int *)(v_rip + 9181334)) & (0x800ULL)) == 0) goto loc_006430FF;
loc_006430EC:
    result = ExAcquireRundownProtection(v_rip + 9178509, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00643138;
loc_006430FF:
    goto loc_00643122;
loc_00643108:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00643122:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00643108;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9178445;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwModifyDriverEntry(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_006431AD;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9181029)) != 0) goto loc_00643161;
    if (((*(unsigned int *)(v_rip + 9181217)) & (0x800ULL)) == 0) goto loc_00643174;
loc_00643161:
    result = ExAcquireRundownProtection(v_rip + 9178392, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006431AD;
loc_00643174:
    v_rsi = (result) + (48);
    goto loc_00643197;
loc_0064317D:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00643197:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064317D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9178328;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwModifyDriverEntryWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
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
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(result + 90, a2, a3, a4);
    if (result == 0) goto loc_00643138;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006430C1;
    v_stack_m28 = v_stack_p0;
    goto loc_006430CF;
loc_006430C1:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C17DA)) != 0) goto loc_006430EC;
    if (((*(uint32_t *)(v_rip + 0x8C1896)) & (0x800ULL)) == 0) goto loc_006430FF;
loc_006430EC:
    result = ExAcquireRundownProtection(v_rip + 9178509, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00643138;
loc_006430FF:
    goto loc_00643122;
loc_00643108:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00643122:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00643108;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9178445;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ZwModifyDriverEntry(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_006431AD;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C1765)) != 0) goto loc_00643161;
    if (((*(uint32_t *)(v_rip + 0x8C1821)) & (0x800ULL)) == 0) goto loc_00643174;
loc_00643161:
    result = ExAcquireRundownProtection(v_rip + 9178392, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006431AD;
loc_00643174:
    local_rsi = (result) + (48);
    goto loc_00643197;
loc_0064317D:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00643197:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064317D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9178328;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00643070&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00643070[BB_00643070]
  bb_006430AE[BB_006430AE]
  bb_006430B5[BB_006430B5]
  bb_006430C1[BB_006430C1]
  bb_006430C5[BB_006430C5]
  bb_006430CF[BB_006430CF]
  bb_006430E0[BB_006430E0]
  bb_006430EC[BB_006430EC]
  bb_006430FF[BB_006430FF]
  bb_00643108[BB_00643108]
  bb_00643111[BB_00643111]
  bb_0064311F[BB_0064311F]
  bb_00643122[BB_00643122]
  bb_00643127[BB_00643127]
  bb_0064312C[BB_0064312C]
  bb_00643138[BB_00643138]
  bb_00643149[BB_00643149]
  bb_00643155[BB_00643155]
  bb_00643161[BB_00643161]
  bb_00643174[BB_00643174]
  bb_0064317D[BB_0064317D]
  bb_00643186[BB_00643186]
  bb_00643194[BB_00643194]
  bb_00643197[BB_00643197]
  bb_0064319C[BB_0064319C]
  bb_006431A1[BB_006431A1]
  bb_006431AD[BB_006431AD]
  bb_006431CC[BB_006431CC]
  bb_00643070 -->|branch| bb_00643138
  bb_00643070 -->|fallthrough| bb_006430AE
  bb_006430AE -->|branch| bb_006430C1
  bb_006430AE -->|fallthrough| bb_006430B5
  bb_006430B5 -->|branch| bb_006430CF
  bb_006430C1 -->|branch| bb_006430CF
  bb_006430C1 -->|fallthrough| bb_006430C5
  bb_006430C5 -->|flow| bb_006430CF
  bb_006430CF -->|branch| bb_006430EC
  bb_006430CF -->|fallthrough| bb_006430E0
  bb_006430E0 -->|branch| bb_006430FF
  bb_006430E0 -->|fallthrough| bb_006430EC
  bb_006430EC -->|branch| bb_00643138
  bb_006430EC -->|fallthrough| bb_006430FF
  bb_006430FF -->|branch| bb_00643122
  bb_00643108 -->|branch| bb_0064311F
  bb_00643108 -->|fallthrough| bb_00643111
  bb_00643111 -->|flow| bb_0064311F
  bb_0064311F -->|flow| bb_00643122
  bb_00643122 -->|branch| bb_00643108
  bb_00643122 -->|fallthrough| bb_00643127
  bb_00643127 -->|branch| bb_00643138
  bb_00643127 -->|fallthrough| bb_0064312C
  bb_0064312C -->|flow| bb_00643138
  bb_00643138 -->|branch| bb_006431AD
  bb_00643138 -->|fallthrough| bb_00643149
  bb_00643149 -->|branch| bb_00643161
  bb_00643149 -->|fallthrough| bb_00643155
  bb_00643155 -->|branch| bb_00643174
  bb_00643155 -->|fallthrough| bb_00643161
  bb_00643161 -->|branch| bb_006431AD
  bb_00643161 -->|fallthrough| bb_00643174
  bb_00643174 -->|branch| bb_00643197
  bb_0064317D -->|branch| bb_00643194
  bb_0064317D -->|fallthrough| bb_00643186
  bb_00643186 -->|flow| bb_00643194
  bb_00643194 -->|flow| bb_00643197
  bb_00643197 -->|branch| bb_0064317D
  bb_00643197 -->|fallthrough| bb_0064319C
  bb_0064319C -->|branch| bb_006431AD
  bb_0064319C -->|fallthrough| bb_006431A1
  bb_006431A1 -->|flow| bb_006431AD
```
