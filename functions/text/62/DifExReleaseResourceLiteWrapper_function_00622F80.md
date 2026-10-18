# DifExReleaseResourceLiteWrapper

- RVA: `0x00622F80`–`0x006230D0` (길이 `336` bytes)
- VA: `0x0000000140622F80`
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
- `0x00622FA8` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00622FD0` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00622FFE` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623025` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062303E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00623046` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0062306F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00623096` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006230AF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00622FE2` → RVA `0x00F048B8` (`.data`; read)
- `0x00622FEB` → RVA `0x00F04980` (`.data`; read)
- `0x00622FF7` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00622F80  48 8B C4                        mov rax, rsp
00622F83  48 89 58 08                     mov qword ptr [rax + 8], rbx
00622F87  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00622F8B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00622F8F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00622F93  41 56                           push r14
00622F95  48 83 EC 30                     sub rsp, 0x30
00622F99  48 8B E9                        mov rbp, rcx
00622F9C  0F 57 C0                        xorps xmm0, xmm0
00622F9F  B9 81 01 00 00                  mov ecx, 0x181
00622FA4  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00622FA8  E8 87 2A E7 FF                  call 0x140495a34
00622FAD  48 8B F8                        mov rdi, rax
00622FB0  48 85 C0                        test rax, rax
00622FB3  0F 84 8A 00 00 00               je 0x140623043
00622FB9  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00622FBC  A8 18                           test al, 0x18
00622FBE  74 0C                           je 0x140622fcc
00622FC0  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00622FC5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00622FCA  EB 0E                           jmp 0x140622fda
00622FCC  A8 04                           test al, 4
00622FCE  74 0A                           je 0x140622fda
00622FD0  E8 33 0C EB FF                  call 0x1404d3c08
00622FD5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00622FDA  40 32 F6                        xor sil, sil
00622FDD  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00622FE2  40 38 35 CF 18 8E 00            cmp byte ptr [rip + 0x8e18cf], sil
00622FE9  75 0C                           jne 0x140622ff7
00622FEB  F7 05 8B 19 8E 00 00 08 00 00   test dword ptr [rip + 0x8e198b], 0x800
00622FF5  74 13                           je 0x14062300a
00622FF7  48 8D 0D 82 0E 8E 00            lea rcx, [rip + 0x8e0e82]
00622FFE  E8 1D 36 BF FF                  call 0x140216620
00623003  40 8A F0                        mov sil, al
00623006  84 C0                           test al, al
00623008  74 39                           je 0x140623043
0062300A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0062300E  49 8B 1E                        mov rbx, qword ptr [r14]
00623011  EB 1A                           jmp 0x14062302d
00623013  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623017  48 85 C0                        test rax, rax
0062301A  74 0E                           je 0x14062302a
0062301C  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623020  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623025  E8 A6 7A 09 00                  call 0x1406baad0
0062302A  48 8B 1B                        mov rbx, qword ptr [rbx]
0062302D  49 3B DE                        cmp rbx, r14
00623030  75 E1                           jne 0x140623013
00623032  40 84 F6                        test sil, sil
00623035  74 0C                           je 0x140623043
00623037  48 8D 0D 42 0E 8E 00            lea rcx, [rip + 0x8e0e42]
0062303E  E8 3D 6E D2 FF                  call 0x140349e80
00623043  48 8B CD                        mov rcx, rbp
00623046  E8 C5 C9 C3 FF                  call 0x14025fa10
0062304B  48 85 FF                        test rdi, rdi
0062304E  74 64                           je 0x1406230b4
00623050  40 32 F6                        xor sil, sil
00623053  40 38 35 5E 18 8E 00            cmp byte ptr [rip + 0x8e185e], sil
0062305A  75 0C                           jne 0x140623068
0062305C  F7 05 1A 19 8E 00 00 08 00 00   test dword ptr [rip + 0x8e191a], 0x800
00623066  74 13                           je 0x14062307b
00623068  48 8D 0D 11 0E 8E 00            lea rcx, [rip + 0x8e0e11]
0062306F  E8 AC 35 BF FF                  call 0x140216620
00623074  40 8A F0                        mov sil, al
00623077  84 C0                           test al, al
00623079  74 39                           je 0x1406230b4
0062307B  48 83 C7 30                     add rdi, 0x30
0062307F  48 8B 1F                        mov rbx, qword ptr [rdi]
00623082  EB 1A                           jmp 0x14062309e
00623084  48 8D 43 F0                     lea rax, [rbx - 0x10]
00623088  48 85 C0                        test rax, rax
0062308B  74 0E                           je 0x14062309b
0062308D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00623091  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00623096  E8 35 7A 09 00                  call 0x1406baad0
0062309B  48 8B 1B                        mov rbx, qword ptr [rbx]
0062309E  48 3B DF                        cmp rbx, rdi
006230A1  75 E1                           jne 0x140623084
006230A3  40 84 F6                        test sil, sil
006230A6  74 0C                           je 0x1406230b4
006230A8  48 8D 0D D1 0D 8E 00            lea rcx, [rip + 0x8e0dd1]
006230AF  E8 CC 6D D2 FF                  call 0x140349e80
006230B4  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
006230B9  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
006230BE  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
006230C3  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
006230C8  48 83 C4 30                     add rsp, 0x30
006230CC  41 5E                           pop r14
006230CE  C3                              ret
006230CF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExReleaseResourceLiteWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(385, a2, a3, a4);
    if (result == 0) goto loc_00623043;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00622FCC;
    v_stack_m18 = v_stack_p0;
    goto loc_00622FDA;
loc_00622FCC:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    v_rsi = 0;
    v_stack_m10 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9312463)) != 0) goto loc_00622FF7;
    if (((*(unsigned int *)(v_rip + 9312651)) & (0x800ULL)) == 0) goto loc_0062300A;
loc_00622FF7:
    result = ExAcquireRundownProtection(v_rip + 9309826, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00623043;
loc_0062300A:
    goto loc_0062302D;
loc_00623013:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062302D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00623013;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9309762;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(a1, a2, a3, a4);
    if (result == 0) goto loc_006230B4;
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9312350)) != 0) goto loc_00623068;
    if (((*(unsigned int *)(v_rip + 9312538)) & (0x800ULL)) == 0) goto loc_0062307B;
loc_00623068:
    result = ExAcquireRundownProtection(v_rip + 9309713, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006230B4;
loc_0062307B:
    v_rdi = (result) + (48);
    goto loc_0062309E;
loc_00623084:
    result = *(unsigned __int64 *)(v_rdi) - 16;
    if (*(unsigned __int64 *)(v_rdi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi) - 16 + 8);
        a1 = v_stack_m18;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062309E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi))) != v_rdi) goto loc_00623084;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9309649;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExReleaseResourceLiteWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(385, a2, a3, a4);
    if (result == 0) goto loc_00623043;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00622FCC;
    v_stack_m18 = v_stack_p0;
    goto loc_00622FDA;
loc_00622FCC:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m18 = result;
    }
    local_rsi = 0;
    v_stack_m10 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E18CF)) != 0) goto loc_00622FF7;
    if (((*(uint32_t *)(v_rip + 0x8E198B)) & (0x800ULL)) == 0) goto loc_0062300A;
loc_00622FF7:
    result = ExAcquireRundownProtection(v_rip + 9309826, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00623043;
loc_0062300A:
    goto loc_0062302D;
loc_00623013:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062302D:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00623013;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9309762;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(Arg1, a2, a3, a4);
    if (result == 0) goto loc_006230B4;
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E185E)) != 0) goto loc_00623068;
    if (((*(uint32_t *)(v_rip + 0x8E191A)) & (0x800ULL)) == 0) goto loc_0062307B;
loc_00623068:
    result = ExAcquireRundownProtection(v_rip + 9309713, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006230B4;
loc_0062307B:
    local_rdi = (result) + (48);
    goto loc_0062309E;
loc_00623084:
    result = *(uint64_t *)(local_rdi) - 16;
    if (*(uint64_t *)(local_rdi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rdi) - 0x10 + 0x8);
        Arg1 = v_stack_m18;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062309E:
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi))) != local_rdi) goto loc_00623084;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9309649;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00622F80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00622F80[BB_00622F80]
  bb_00622FB9[BB_00622FB9]
  bb_00622FC0[BB_00622FC0]
  bb_00622FCC[BB_00622FCC]
  bb_00622FD0[BB_00622FD0]
  bb_00622FDA[BB_00622FDA]
  bb_00622FEB[BB_00622FEB]
  bb_00622FF7[BB_00622FF7]
  bb_0062300A[BB_0062300A]
  bb_00623013[BB_00623013]
  bb_0062301C[BB_0062301C]
  bb_0062302A[BB_0062302A]
  bb_0062302D[BB_0062302D]
  bb_00623032[BB_00623032]
  bb_00623037[BB_00623037]
  bb_00623043[BB_00623043]
  bb_00623050[BB_00623050]
  bb_0062305C[BB_0062305C]
  bb_00623068[BB_00623068]
  bb_0062307B[BB_0062307B]
  bb_00623084[BB_00623084]
  bb_0062308D[BB_0062308D]
  bb_0062309B[BB_0062309B]
  bb_0062309E[BB_0062309E]
  bb_006230A3[BB_006230A3]
  bb_006230A8[BB_006230A8]
  bb_006230B4[BB_006230B4]
  bb_006230CF[BB_006230CF]
  bb_00622F80 -->|branch| bb_00623043
  bb_00622F80 -->|fallthrough| bb_00622FB9
  bb_00622FB9 -->|branch| bb_00622FCC
  bb_00622FB9 -->|fallthrough| bb_00622FC0
  bb_00622FC0 -->|branch| bb_00622FDA
  bb_00622FCC -->|branch| bb_00622FDA
  bb_00622FCC -->|fallthrough| bb_00622FD0
  bb_00622FD0 -->|flow| bb_00622FDA
  bb_00622FDA -->|branch| bb_00622FF7
  bb_00622FDA -->|fallthrough| bb_00622FEB
  bb_00622FEB -->|branch| bb_0062300A
  bb_00622FEB -->|fallthrough| bb_00622FF7
  bb_00622FF7 -->|branch| bb_00623043
  bb_00622FF7 -->|fallthrough| bb_0062300A
  bb_0062300A -->|branch| bb_0062302D
  bb_00623013 -->|branch| bb_0062302A
  bb_00623013 -->|fallthrough| bb_0062301C
  bb_0062301C -->|flow| bb_0062302A
  bb_0062302A -->|flow| bb_0062302D
  bb_0062302D -->|branch| bb_00623013
  bb_0062302D -->|fallthrough| bb_00623032
  bb_00623032 -->|branch| bb_00623043
  bb_00623032 -->|fallthrough| bb_00623037
  bb_00623037 -->|flow| bb_00623043
  bb_00623043 -->|branch| bb_006230B4
  bb_00623043 -->|fallthrough| bb_00623050
  bb_00623050 -->|branch| bb_00623068
  bb_00623050 -->|fallthrough| bb_0062305C
  bb_0062305C -->|branch| bb_0062307B
  bb_0062305C -->|fallthrough| bb_00623068
  bb_00623068 -->|branch| bb_006230B4
  bb_00623068 -->|fallthrough| bb_0062307B
  bb_0062307B -->|branch| bb_0062309E
  bb_00623084 -->|branch| bb_0062309B
  bb_00623084 -->|fallthrough| bb_0062308D
  bb_0062308D -->|flow| bb_0062309B
  bb_0062309B -->|flow| bb_0062309E
  bb_0062309E -->|branch| bb_00623084
  bb_0062309E -->|fallthrough| bb_006230A3
  bb_006230A3 -->|branch| bb_006230B4
  bb_006230A3 -->|fallthrough| bb_006230A8
  bb_006230A8 -->|flow| bb_006230B4
```
