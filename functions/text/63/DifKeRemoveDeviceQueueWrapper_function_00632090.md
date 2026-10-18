# DifKeRemoveDeviceQueueWrapper

- RVA: `0x00632090`–`0x006321F1` (길이 `353` bytes)
- VA: `0x0000000140632090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006320BF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006320E7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00632115` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063213C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00632155` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063215D` → [KeRemoveDeviceQueue](../3D/KeRemoveDeviceQueue_function_003DF890.md) (function, `0x003DF890`)
- `0x0063218B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006321B2` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006321CB` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006320F9` → RVA `0x00F048B8` (`.data`; read)
- `0x00632102` → RVA `0x00F04980` (`.data`; read)
- `0x0063210E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00632090  4C 8B DC                        mov r11, rsp
00632093  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00632097  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063209B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063209F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006320A3  41 56                           push r14
006320A5  48 83 EC 40                     sub rsp, 0x40
006320A9  33 C0                           xor eax, eax
006320AB  0F 57 C0                        xorps xmm0, xmm0
006320AE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
006320B3  48 8B E9                        mov rbp, rcx
006320B6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
006320BA  B9 FF 00 00 00                  mov ecx, 0xff
006320BF  E8 70 39 E6 FF                  call 0x140495a34
006320C4  48 8B F0                        mov rsi, rax
006320C7  48 85 C0                        test rax, rax
006320CA  0F 84 8A 00 00 00               je 0x14063215a
006320D0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
006320D3  A8 18                           test al, 0x18
006320D5  74 0C                           je 0x1406320e3
006320D7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
006320DC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006320E1  EB 0E                           jmp 0x1406320f1
006320E3  A8 04                           test al, 4
006320E5  74 0A                           je 0x1406320f1
006320E7  E8 1C 1B EA FF                  call 0x1404d3c08
006320EC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006320F1  40 32 FF                        xor dil, dil
006320F4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006320F9  40 38 3D B8 27 8D 00            cmp byte ptr [rip + 0x8d27b8], dil
00632100  75 0C                           jne 0x14063210e
00632102  F7 05 74 28 8D 00 00 08 00 00   test dword ptr [rip + 0x8d2874], 0x800
0063210C  74 13                           je 0x140632121
0063210E  48 8D 0D 6B 1D 8D 00            lea rcx, [rip + 0x8d1d6b]
00632115  E8 06 45 BE FF                  call 0x140216620
0063211A  40 8A F8                        mov dil, al
0063211D  84 C0                           test al, al
0063211F  74 39                           je 0x14063215a
00632121  4C 8D 76 20                     lea r14, [rsi + 0x20]
00632125  49 8B 1E                        mov rbx, qword ptr [r14]
00632128  EB 1A                           jmp 0x140632144
0063212A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063212E  48 85 C0                        test rax, rax
00632131  74 0E                           je 0x140632141
00632133  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632137  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063213C  E8 8F 89 08 00                  call 0x1406baad0
00632141  48 8B 1B                        mov rbx, qword ptr [rbx]
00632144  49 3B DE                        cmp rbx, r14
00632147  75 E1                           jne 0x14063212a
00632149  40 84 FF                        test dil, dil
0063214C  74 0C                           je 0x14063215a
0063214E  48 8D 0D 2B 1D 8D 00            lea rcx, [rip + 0x8d1d2b]
00632155  E8 26 7D D1 FF                  call 0x140349e80
0063215A  48 8B CD                        mov rcx, rbp
0063215D  E8 2E D7 DA FF                  call 0x1403df890
00632162  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00632167  48 85 F6                        test rsi, rsi
0063216A  74 64                           je 0x1406321d0
0063216C  40 32 FF                        xor dil, dil
0063216F  40 38 3D 42 27 8D 00            cmp byte ptr [rip + 0x8d2742], dil
00632176  75 0C                           jne 0x140632184
00632178  F7 05 FE 27 8D 00 00 08 00 00   test dword ptr [rip + 0x8d27fe], 0x800
00632182  74 13                           je 0x140632197
00632184  48 8D 0D F5 1C 8D 00            lea rcx, [rip + 0x8d1cf5]
0063218B  E8 90 44 BE FF                  call 0x140216620
00632190  40 8A F8                        mov dil, al
00632193  84 C0                           test al, al
00632195  74 39                           je 0x1406321d0
00632197  48 83 C6 30                     add rsi, 0x30
0063219B  48 8B 1E                        mov rbx, qword ptr [rsi]
0063219E  EB 1A                           jmp 0x1406321ba
006321A0  48 8D 43 F0                     lea rax, [rbx - 0x10]
006321A4  48 85 C0                        test rax, rax
006321A7  74 0E                           je 0x1406321b7
006321A9  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006321AD  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006321B2  E8 19 89 08 00                  call 0x1406baad0
006321B7  48 8B 1B                        mov rbx, qword ptr [rbx]
006321BA  48 3B DE                        cmp rbx, rsi
006321BD  75 E1                           jne 0x1406321a0
006321BF  40 84 FF                        test dil, dil
006321C2  74 0C                           je 0x1406321d0
006321C4  48 8D 0D B5 1C 8D 00            lea rcx, [rip + 0x8d1cb5]
006321CB  E8 B0 7C D1 FF                  call 0x140349e80
006321D0  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006321D5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
006321DA  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
006321DF  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
006321E4  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
006321E9  48 83 C4 40                     add rsp, 0x40
006321ED  41 5E                           pop r14
006321EF  C3                              ret
006321F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeRemoveDeviceQueueWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
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
    result = DifGetAPIThunkContextById(255, a2, a3, a4);
    if (result == 0) goto loc_0063215A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006320E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006320F1;
loc_006320E3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9250744)) != 0) goto loc_0063210E;
    if (((*(unsigned int *)(v_rip + 9250932)) & (0x800ULL)) == 0) goto loc_00632121;
loc_0063210E:
    result = ExAcquireRundownProtection(v_rip + 9248107, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063215A;
loc_00632121:
    goto loc_00632144;
loc_0063212A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632144:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063212A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9248043;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = KeRemoveDeviceQueue(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006321D0;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9250626)) != 0) goto loc_00632184;
    if (((*(unsigned int *)(v_rip + 9250814)) & (0x800ULL)) == 0) goto loc_00632197;
loc_00632184:
    result = ExAcquireRundownProtection(v_rip + 9247989, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006321D0;
loc_00632197:
    v_rsi = (result) + (48);
    goto loc_006321BA;
loc_006321A0:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006321BA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006321A0;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9247925;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeRemoveDeviceQueueWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(255, a2, a3, a4);
    if (result == 0) goto loc_0063215A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006320E3;
    v_stack_m28 = v_stack_p0;
    goto loc_006320F1;
loc_006320E3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D27B8)) != 0) goto loc_0063210E;
    if (((*(uint32_t *)(v_rip + 0x8D2874)) & (0x800ULL)) == 0) goto loc_00632121;
loc_0063210E:
    result = ExAcquireRundownProtection(v_rip + 9248107, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063215A;
loc_00632121:
    goto loc_00632144;
loc_0063212A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00632144:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063212A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9248043;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = KeRemoveDeviceQueue(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_006321D0;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D2742)) != 0) goto loc_00632184;
    if (((*(uint32_t *)(v_rip + 0x8D27FE)) & (0x800ULL)) == 0) goto loc_00632197;
loc_00632184:
    result = ExAcquireRundownProtection(v_rip + 9247989, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006321D0;
loc_00632197:
    local_rsi = (result) + (48);
    goto loc_006321BA;
loc_006321A0:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006321BA:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006321A0;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9247925;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00632090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00632090[BB_00632090]
  bb_006320D0[BB_006320D0]
  bb_006320D7[BB_006320D7]
  bb_006320E3[BB_006320E3]
  bb_006320E7[BB_006320E7]
  bb_006320F1[BB_006320F1]
  bb_00632102[BB_00632102]
  bb_0063210E[BB_0063210E]
  bb_00632121[BB_00632121]
  bb_0063212A[BB_0063212A]
  bb_00632133[BB_00632133]
  bb_00632141[BB_00632141]
  bb_00632144[BB_00632144]
  bb_00632149[BB_00632149]
  bb_0063214E[BB_0063214E]
  bb_0063215A[BB_0063215A]
  bb_0063216C[BB_0063216C]
  bb_00632178[BB_00632178]
  bb_00632184[BB_00632184]
  bb_00632197[BB_00632197]
  bb_006321A0[BB_006321A0]
  bb_006321A9[BB_006321A9]
  bb_006321B7[BB_006321B7]
  bb_006321BA[BB_006321BA]
  bb_006321BF[BB_006321BF]
  bb_006321C4[BB_006321C4]
  bb_006321D0[BB_006321D0]
  bb_006321F0[BB_006321F0]
  bb_00632090 -->|branch| bb_0063215A
  bb_00632090 -->|fallthrough| bb_006320D0
  bb_006320D0 -->|branch| bb_006320E3
  bb_006320D0 -->|fallthrough| bb_006320D7
  bb_006320D7 -->|branch| bb_006320F1
  bb_006320E3 -->|branch| bb_006320F1
  bb_006320E3 -->|fallthrough| bb_006320E7
  bb_006320E7 -->|flow| bb_006320F1
  bb_006320F1 -->|branch| bb_0063210E
  bb_006320F1 -->|fallthrough| bb_00632102
  bb_00632102 -->|branch| bb_00632121
  bb_00632102 -->|fallthrough| bb_0063210E
  bb_0063210E -->|branch| bb_0063215A
  bb_0063210E -->|fallthrough| bb_00632121
  bb_00632121 -->|branch| bb_00632144
  bb_0063212A -->|branch| bb_00632141
  bb_0063212A -->|fallthrough| bb_00632133
  bb_00632133 -->|flow| bb_00632141
  bb_00632141 -->|flow| bb_00632144
  bb_00632144 -->|branch| bb_0063212A
  bb_00632144 -->|fallthrough| bb_00632149
  bb_00632149 -->|branch| bb_0063215A
  bb_00632149 -->|fallthrough| bb_0063214E
  bb_0063214E -->|flow| bb_0063215A
  bb_0063215A -->|branch| bb_006321D0
  bb_0063215A -->|fallthrough| bb_0063216C
  bb_0063216C -->|branch| bb_00632184
  bb_0063216C -->|fallthrough| bb_00632178
  bb_00632178 -->|branch| bb_00632197
  bb_00632178 -->|fallthrough| bb_00632184
  bb_00632184 -->|branch| bb_006321D0
  bb_00632184 -->|fallthrough| bb_00632197
  bb_00632197 -->|branch| bb_006321BA
  bb_006321A0 -->|branch| bb_006321B7
  bb_006321A0 -->|fallthrough| bb_006321A9
  bb_006321A9 -->|flow| bb_006321B7
  bb_006321B7 -->|flow| bb_006321BA
  bb_006321BA -->|branch| bb_006321A0
  bb_006321BA -->|fallthrough| bb_006321BF
  bb_006321BF -->|branch| bb_006321D0
  bb_006321BF -->|fallthrough| bb_006321C4
  bb_006321C4 -->|flow| bb_006321D0
```
