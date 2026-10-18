# DifExInitializeResourceLiteWrapper

- RVA: `0x006210C0`–`0x00621222` (길이 `354` bytes)
- VA: `0x00000001406210C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `95`개 명령, `354/354` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006210EF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00621117` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00621145` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062116C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00621185` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00621190` → [ExInitializeResourceLite2](../41/ExInitializeResourceLite2_function_0041F710.md) (function, `0x0041F710`)
- `0x006211BD` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006211E4` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006211FD` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00621129` → RVA `0x00F048B8` (`.data`; read)
- `0x00621132` → RVA `0x00F04980` (`.data`; read)
- `0x0062113E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006210C0  4C 8B DC                        mov r11, rsp
006210C3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006210C7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006210CB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006210CF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006210D3  41 56                           push r14
006210D5  48 83 EC 40                     sub rsp, 0x40
006210D9  33 C0                           xor eax, eax
006210DB  0F 57 C0                        xorps xmm0, xmm0
006210DE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006210E3  48 8B E9                        mov rbp, rcx
006210E6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006210EA  B9 8C 01 00 00                  mov ecx, 0x18c
006210EF  E8 40 49 E7 FF                  call 0x140495a34
006210F4  48 8B F0                        mov rsi, rax
006210F7  48 85 C0                        test rax, rax
006210FA  0F 84 8A 00 00 00               je 0x14062118a
00621100  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00621103  A8 18                           test al, 0x18
00621105  74 0C                           je 0x140621113
00621107  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062110C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00621111  EB 0E                           jmp 0x140621121
00621113  A8 04                           test al, 4
00621115  74 0A                           je 0x140621121
00621117  E8 EC 2A EB FF                  call 0x1404d3c08
0062111C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00621121  40 32 FF                        xor dil, dil
00621124  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00621129  40 38 3D 88 37 8E 00            cmp byte ptr [rip + 0x8e3788], dil
00621130  75 0C                           jne 0x14062113e
00621132  F7 05 44 38 8E 00 00 08 00 00   test dword ptr [rip + 0x8e3844], 0x800
0062113C  74 13                           je 0x140621151
0062113E  48 8D 0D 3B 2D 8E 00            lea rcx, [rip + 0x8e2d3b]
00621145  E8 D6 54 BF FF                  call 0x140216620
0062114A  40 8A F8                        mov dil, al
0062114D  84 C0                           test al, al
0062114F  74 39                           je 0x14062118a
00621151  4C 8D 76 20                     lea r14, [rsi + 0x20]
00621155  49 8B 1E                        mov rbx, qword ptr [r14]
00621158  EB 1A                           jmp 0x140621174
0062115A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062115E  48 85 C0                        test rax, rax
00621161  74 0E                           je 0x140621171
00621163  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621167  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062116C  E8 5F 99 09 00                  call 0x1406baad0
00621171  48 8B 1B                        mov rbx, qword ptr [rbx]
00621174  49 3B DE                        cmp rbx, r14
00621177  75 E1                           jne 0x14062115a
00621179  40 84 FF                        test dil, dil
0062117C  74 0C                           je 0x14062118a
0062117E  48 8D 0D FB 2C 8E 00            lea rcx, [rip + 0x8e2cfb]
00621185  E8 F6 8C D2 FF                  call 0x140349e80
0062118A  83 CA FF                        or edx, 0xffffffff
0062118D  48 8B CD                        mov rcx, rbp
00621190  E8 7B E5 DF FF                  call 0x14041f710
00621195  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00621199  48 85 F6                        test rsi, rsi
0062119C  74 64                           je 0x140621202
0062119E  40 32 FF                        xor dil, dil
006211A1  40 38 3D 10 37 8E 00            cmp byte ptr [rip + 0x8e3710], dil
006211A8  75 0C                           jne 0x1406211b6
006211AA  F7 05 CC 37 8E 00 00 08 00 00   test dword ptr [rip + 0x8e37cc], 0x800
006211B4  74 13                           je 0x1406211c9
006211B6  48 8D 0D C3 2C 8E 00            lea rcx, [rip + 0x8e2cc3]
006211BD  E8 5E 54 BF FF                  call 0x140216620
006211C2  40 8A F8                        mov dil, al
006211C5  84 C0                           test al, al
006211C7  74 39                           je 0x140621202
006211C9  48 83 C6 30                     add rsi, 0x30
006211CD  48 8B 1E                        mov rbx, qword ptr [rsi]
006211D0  EB 1A                           jmp 0x1406211ec
006211D2  48 8D 43 F0                     lea rax, [rbx - 0x10]
006211D6  48 85 C0                        test rax, rax
006211D9  74 0E                           je 0x1406211e9
006211DB  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006211DF  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006211E4  E8 E7 98 09 00                  call 0x1406baad0
006211E9  48 8B 1B                        mov rbx, qword ptr [rbx]
006211EC  48 3B DE                        cmp rbx, rsi
006211EF  75 E1                           jne 0x1406211d2
006211F1  40 84 FF                        test dil, dil
006211F4  74 0C                           je 0x140621202
006211F6  48 8D 0D 83 2C 8E 00            lea rcx, [rip + 0x8e2c83]
006211FD  E8 7E 8C D2 FF                  call 0x140349e80
00621202  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00621206  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062120B  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00621210  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00621215  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062121A  48 83 C4 40                     add rsp, 0x40
0062121E  41 5E                           pop r14
00621220  C3                              ret
00621221  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExInitializeResourceLiteWrapper(__int64 a1, int a2)
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
    result = DifGetAPIThunkContextById(396, a2, a3, a4);
    if (result == 0) goto loc_0062118A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00621113;
    v_stack_m28 = v_stack_p0;
    goto loc_00621121;
loc_00621113:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9320328)) != 0) goto loc_0062113E;
    if (((*(unsigned int *)(v_rip + 9320516)) & (0x800ULL)) == 0) goto loc_00621151;
loc_0062113E:
    result = ExAcquireRundownProtection(v_rip + 9317691, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062118A;
loc_00621151:
    goto loc_00621174;
loc_0062115A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621174:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062115A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9317627;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = ExInitializeResourceLite2(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_00621202;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9320208)) != 0) goto loc_006211B6;
    if (((*(unsigned int *)(v_rip + 9320396)) & (0x800ULL)) == 0) goto loc_006211C9;
loc_006211B6:
    result = ExAcquireRundownProtection(v_rip + 9317571, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00621202;
loc_006211C9:
    v_rsi = (result) + (48);
    goto loc_006211EC;
loc_006211D2:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006211EC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006211D2;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9317507;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifExInitializeResourceLiteWrapper(int64_t Arg1, int32_t Arg2)
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
    result = DifGetAPIThunkContextById(396, Arg2, a3, a4);
    if (result == 0) goto loc_0062118A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00621113;
    v_stack_m28 = v_stack_p0;
    goto loc_00621121;
loc_00621113:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E3788)) != 0) goto loc_0062113E;
    if (((*(uint32_t *)(v_rip + 0x8E3844)) & (0x800ULL)) == 0) goto loc_00621151;
loc_0062113E:
    result = ExAcquireRundownProtection(v_rip + 9317691, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062118A;
loc_00621151:
    goto loc_00621174;
loc_0062115A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00621174:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062115A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9317627;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = ExInitializeResourceLite2(Arg1, Arg2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_00621202;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E3710)) != 0) goto loc_006211B6;
    if (((*(uint32_t *)(v_rip + 0x8E37CC)) & (0x800ULL)) == 0) goto loc_006211C9;
loc_006211B6:
    result = ExAcquireRundownProtection(v_rip + 9317571, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00621202;
loc_006211C9:
    local_rsi = (result) + (48);
    goto loc_006211EC;
loc_006211D2:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006211EC:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006211D2;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9317507;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006210C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006210C0[BB_006210C0]
  bb_00621100[BB_00621100]
  bb_00621107[BB_00621107]
  bb_00621113[BB_00621113]
  bb_00621117[BB_00621117]
  bb_00621121[BB_00621121]
  bb_00621132[BB_00621132]
  bb_0062113E[BB_0062113E]
  bb_00621151[BB_00621151]
  bb_0062115A[BB_0062115A]
  bb_00621163[BB_00621163]
  bb_00621171[BB_00621171]
  bb_00621174[BB_00621174]
  bb_00621179[BB_00621179]
  bb_0062117E[BB_0062117E]
  bb_0062118A[BB_0062118A]
  bb_0062119E[BB_0062119E]
  bb_006211AA[BB_006211AA]
  bb_006211B6[BB_006211B6]
  bb_006211C9[BB_006211C9]
  bb_006211D2[BB_006211D2]
  bb_006211DB[BB_006211DB]
  bb_006211E9[BB_006211E9]
  bb_006211EC[BB_006211EC]
  bb_006211F1[BB_006211F1]
  bb_006211F6[BB_006211F6]
  bb_00621202[BB_00621202]
  bb_00621221[BB_00621221]
  bb_006210C0 -->|branch| bb_0062118A
  bb_006210C0 -->|fallthrough| bb_00621100
  bb_00621100 -->|branch| bb_00621113
  bb_00621100 -->|fallthrough| bb_00621107
  bb_00621107 -->|branch| bb_00621121
  bb_00621113 -->|branch| bb_00621121
  bb_00621113 -->|fallthrough| bb_00621117
  bb_00621117 -->|flow| bb_00621121
  bb_00621121 -->|branch| bb_0062113E
  bb_00621121 -->|fallthrough| bb_00621132
  bb_00621132 -->|branch| bb_00621151
  bb_00621132 -->|fallthrough| bb_0062113E
  bb_0062113E -->|branch| bb_0062118A
  bb_0062113E -->|fallthrough| bb_00621151
  bb_00621151 -->|branch| bb_00621174
  bb_0062115A -->|branch| bb_00621171
  bb_0062115A -->|fallthrough| bb_00621163
  bb_00621163 -->|flow| bb_00621171
  bb_00621171 -->|flow| bb_00621174
  bb_00621174 -->|branch| bb_0062115A
  bb_00621174 -->|fallthrough| bb_00621179
  bb_00621179 -->|branch| bb_0062118A
  bb_00621179 -->|fallthrough| bb_0062117E
  bb_0062117E -->|flow| bb_0062118A
  bb_0062118A -->|branch| bb_00621202
  bb_0062118A -->|fallthrough| bb_0062119E
  bb_0062119E -->|branch| bb_006211B6
  bb_0062119E -->|fallthrough| bb_006211AA
  bb_006211AA -->|branch| bb_006211C9
  bb_006211AA -->|fallthrough| bb_006211B6
  bb_006211B6 -->|branch| bb_00621202
  bb_006211B6 -->|fallthrough| bb_006211C9
  bb_006211C9 -->|branch| bb_006211EC
  bb_006211D2 -->|branch| bb_006211E9
  bb_006211D2 -->|fallthrough| bb_006211DB
  bb_006211DB -->|flow| bb_006211E9
  bb_006211E9 -->|flow| bb_006211EC
  bb_006211EC -->|branch| bb_006211D2
  bb_006211EC -->|fallthrough| bb_006211F1
  bb_006211F1 -->|branch| bb_00621202
  bb_006211F1 -->|fallthrough| bb_006211F6
  bb_006211F6 -->|flow| bb_00621202
```
