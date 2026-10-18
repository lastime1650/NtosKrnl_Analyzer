# DifMmUnmapLockedPagesWrapper

- RVA: `0x00636F90`–`0x006370EF` (길이 `351` bytes)
- VA: `0x0000000140636F90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `97`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00636FC1` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00636FE9` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063701C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00637043` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063705C` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00637067` → [MmUnmapLockedPages](../24/MmUnmapLockedPages_function_00246E60.md) (function, `0x00246E60`)
- `0x00637090` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006370B7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006370D0` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00636FFB` → RVA `0x00F048B8` (`.data`; read)
- `0x00637009` → RVA `0x00F04980` (`.data`; read)
- `0x00637015` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00636F90  4C 8B DC                        mov r11, rsp
00636F93  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00636F97  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00636F9B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00636F9F  57                              push rdi
00636FA0  41 56                           push r14
00636FA2  41 57                           push r15
00636FA4  48 83 EC 40                     sub rsp, 0x40
00636FA8  33 C0                           xor eax, eax
00636FAA  0F 57 C0                        xorps xmm0, xmm0
00636FAD  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00636FB2  4C 8B F9                        mov r15, rcx
00636FB5  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00636FB9  B9 D2 00 00 00                  mov ecx, 0xd2
00636FBE  4C 8B F2                        mov r14, rdx
00636FC1  E8 6E EA E5 FF                  call 0x140495a34
00636FC6  48 8B F0                        mov rsi, rax
00636FC9  48 85 C0                        test rax, rax
00636FCC  0F 84 8F 00 00 00               je 0x140637061
00636FD2  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00636FD5  A8 18                           test al, 0x18
00636FD7  74 0C                           je 0x140636fe5
00636FD9  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00636FDE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00636FE3  EB 0E                           jmp 0x140636ff3
00636FE5  A8 04                           test al, 4
00636FE7  74 0A                           je 0x140636ff3
00636FE9  E8 1A CC E9 FF                  call 0x1404d3c08
00636FEE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00636FF3  40 32 ED                        xor bpl, bpl
00636FF6  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00636FFB  40 38 2D B6 D8 8C 00            cmp byte ptr [rip + 0x8cd8b6], bpl
00637002  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00637007  75 0C                           jne 0x140637015
00637009  F7 05 6D D9 8C 00 00 08 00 00   test dword ptr [rip + 0x8cd96d], 0x800
00637013  74 13                           je 0x140637028
00637015  48 8D 0D 64 CE 8C 00            lea rcx, [rip + 0x8cce64]
0063701C  E8 FF F5 BD FF                  call 0x140216620
00637021  40 8A E8                        mov bpl, al
00637024  84 C0                           test al, al
00637026  74 39                           je 0x140637061
00637028  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063702C  48 8B 1F                        mov rbx, qword ptr [rdi]
0063702F  EB 1A                           jmp 0x14063704b
00637031  48 8D 43 F0                     lea rax, [rbx - 0x10]
00637035  48 85 C0                        test rax, rax
00637038  74 0E                           je 0x140637048
0063703A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063703E  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00637043  E8 88 3A 08 00                  call 0x1406baad0
00637048  48 8B 1B                        mov rbx, qword ptr [rbx]
0063704B  48 3B DF                        cmp rbx, rdi
0063704E  75 E1                           jne 0x140637031
00637050  40 84 ED                        test bpl, bpl
00637053  74 0C                           je 0x140637061
00637055  48 8D 0D 24 CE 8C 00            lea rcx, [rip + 0x8cce24]
0063705C  E8 1F 2E D1 FF                  call 0x140349e80
00637061  49 8B D6                        mov rdx, r14
00637064  49 8B CF                        mov rcx, r15
00637067  E8 F4 FD C0 FF                  call 0x140246e60
0063706C  48 85 F6                        test rsi, rsi
0063706F  74 64                           je 0x1406370d5
00637071  40 32 FF                        xor dil, dil
00637074  40 38 3D 3D D8 8C 00            cmp byte ptr [rip + 0x8cd83d], dil
0063707B  75 0C                           jne 0x140637089
0063707D  F7 05 F9 D8 8C 00 00 08 00 00   test dword ptr [rip + 0x8cd8f9], 0x800
00637087  74 13                           je 0x14063709c
00637089  48 8D 0D F0 CD 8C 00            lea rcx, [rip + 0x8ccdf0]
00637090  E8 8B F5 BD FF                  call 0x140216620
00637095  40 8A F8                        mov dil, al
00637098  84 C0                           test al, al
0063709A  74 39                           je 0x1406370d5
0063709C  48 83 C6 30                     add rsi, 0x30
006370A0  48 8B 1E                        mov rbx, qword ptr [rsi]
006370A3  EB 1A                           jmp 0x1406370bf
006370A5  48 8D 43 F0                     lea rax, [rbx - 0x10]
006370A9  48 85 C0                        test rax, rax
006370AC  74 0E                           je 0x1406370bc
006370AE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006370B2  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006370B7  E8 14 3A 08 00                  call 0x1406baad0
006370BC  48 8B 1B                        mov rbx, qword ptr [rbx]
006370BF  48 3B DE                        cmp rbx, rsi
006370C2  75 E1                           jne 0x1406370a5
006370C4  40 84 FF                        test dil, dil
006370C7  74 0C                           je 0x1406370d5
006370C9  48 8D 0D B0 CD 8C 00            lea rcx, [rip + 0x8ccdb0]
006370D0  E8 AB 2D D1 FF                  call 0x140349e80
006370D5  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006370DA  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006370DF  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006370E4  48 83 C4 40                     add rsp, 0x40
006370E8  41 5F                           pop r15
006370EA  41 5E                           pop r14
006370EC  5F                              pop rdi
006370ED  C3                              ret
006370EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmUnmapLockedPagesWrapper(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
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
    result = DifGetAPIThunkContextById(210, a2, a3, a4);
    if (result == 0) goto loc_00637061;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00636FE5;
    v_stack_m38 = v_stack_p0;
    goto loc_00636FF3;
loc_00636FE5:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9230518)) != 0) goto loc_00637015;
    if (((*(unsigned int *)(v_rip + 9230701)) & (0x800ULL)) == 0) goto loc_00637028;
loc_00637015:
    result = ExAcquireRundownProtection(v_rip + 9227876, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00637061;
loc_00637028:
    goto loc_0063704B;
loc_00637031:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063704B:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00637031;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9227812;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmUnmapLockedPages(a1, a2, a3, a4);
    if (result == 0) goto loc_006370D5;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9230397)) != 0) goto loc_00637089;
    if (((*(unsigned int *)(v_rip + 9230585)) & (0x800ULL)) == 0) goto loc_0063709C;
loc_00637089:
    result = ExAcquireRundownProtection(v_rip + 9227760, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006370D5;
loc_0063709C:
    v_rsi = (result) + (48);
    goto loc_006370BF;
loc_006370A5:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006370BF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006370A5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9227696;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmUnmapLockedPagesWrapper(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(210, Arg2, a3, a4);
    if (result == 0) goto loc_00637061;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00636FE5;
    v_stack_m38 = v_stack_p0;
    goto loc_00636FF3;
loc_00636FE5:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8CD8B6)) != 0) goto loc_00637015;
    if (((*(uint32_t *)(v_rip + 0x8CD96D)) & (0x800ULL)) == 0) goto loc_00637028;
loc_00637015:
    result = ExAcquireRundownProtection(v_rip + 9227876, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00637061;
loc_00637028:
    goto loc_0063704B;
loc_00637031:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0063704B:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00637031;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9227812;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = MmUnmapLockedPages(Arg1, Arg2, a3, a4);
    if (result == 0) goto loc_006370D5;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CD83D)) != 0) goto loc_00637089;
    if (((*(uint32_t *)(v_rip + 0x8CD8F9)) & (0x800ULL)) == 0) goto loc_0063709C;
loc_00637089:
    result = ExAcquireRundownProtection(v_rip + 9227760, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006370D5;
loc_0063709C:
    local_rsi = (result) + (48);
    goto loc_006370BF;
loc_006370A5:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_006370BF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006370A5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9227696;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00636F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00636F90[BB_00636F90]
  bb_00636FD2[BB_00636FD2]
  bb_00636FD9[BB_00636FD9]
  bb_00636FE5[BB_00636FE5]
  bb_00636FE9[BB_00636FE9]
  bb_00636FF3[BB_00636FF3]
  bb_00637009[BB_00637009]
  bb_00637015[BB_00637015]
  bb_00637028[BB_00637028]
  bb_00637031[BB_00637031]
  bb_0063703A[BB_0063703A]
  bb_00637048[BB_00637048]
  bb_0063704B[BB_0063704B]
  bb_00637050[BB_00637050]
  bb_00637055[BB_00637055]
  bb_00637061[BB_00637061]
  bb_00637071[BB_00637071]
  bb_0063707D[BB_0063707D]
  bb_00637089[BB_00637089]
  bb_0063709C[BB_0063709C]
  bb_006370A5[BB_006370A5]
  bb_006370AE[BB_006370AE]
  bb_006370BC[BB_006370BC]
  bb_006370BF[BB_006370BF]
  bb_006370C4[BB_006370C4]
  bb_006370C9[BB_006370C9]
  bb_006370D5[BB_006370D5]
  bb_006370EE[BB_006370EE]
  bb_00636F90 -->|branch| bb_00637061
  bb_00636F90 -->|fallthrough| bb_00636FD2
  bb_00636FD2 -->|branch| bb_00636FE5
  bb_00636FD2 -->|fallthrough| bb_00636FD9
  bb_00636FD9 -->|branch| bb_00636FF3
  bb_00636FE5 -->|branch| bb_00636FF3
  bb_00636FE5 -->|fallthrough| bb_00636FE9
  bb_00636FE9 -->|flow| bb_00636FF3
  bb_00636FF3 -->|branch| bb_00637015
  bb_00636FF3 -->|fallthrough| bb_00637009
  bb_00637009 -->|branch| bb_00637028
  bb_00637009 -->|fallthrough| bb_00637015
  bb_00637015 -->|branch| bb_00637061
  bb_00637015 -->|fallthrough| bb_00637028
  bb_00637028 -->|branch| bb_0063704B
  bb_00637031 -->|branch| bb_00637048
  bb_00637031 -->|fallthrough| bb_0063703A
  bb_0063703A -->|flow| bb_00637048
  bb_00637048 -->|flow| bb_0063704B
  bb_0063704B -->|branch| bb_00637031
  bb_0063704B -->|fallthrough| bb_00637050
  bb_00637050 -->|branch| bb_00637061
  bb_00637050 -->|fallthrough| bb_00637055
  bb_00637055 -->|flow| bb_00637061
  bb_00637061 -->|branch| bb_006370D5
  bb_00637061 -->|fallthrough| bb_00637071
  bb_00637071 -->|branch| bb_00637089
  bb_00637071 -->|fallthrough| bb_0063707D
  bb_0063707D -->|branch| bb_0063709C
  bb_0063707D -->|fallthrough| bb_00637089
  bb_00637089 -->|branch| bb_006370D5
  bb_00637089 -->|fallthrough| bb_0063709C
  bb_0063709C -->|branch| bb_006370BF
  bb_006370A5 -->|branch| bb_006370BC
  bb_006370A5 -->|fallthrough| bb_006370AE
  bb_006370AE -->|flow| bb_006370BC
  bb_006370BC -->|flow| bb_006370BF
  bb_006370BF -->|branch| bb_006370A5
  bb_006370BF -->|fallthrough| bb_006370C4
  bb_006370C4 -->|branch| bb_006370D5
  bb_006370C4 -->|fallthrough| bb_006370C9
  bb_006370C9 -->|flow| bb_006370D5
```
