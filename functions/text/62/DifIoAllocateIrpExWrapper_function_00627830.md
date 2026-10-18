# DifIoAllocateIrpExWrapper

- RVA: `0x00627830`–`0x006279BF` (길이 `399` bytes)
- VA: `0x0000000140627830`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `114`개 명령, `399/399` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00627872` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062789A` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006278D6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006278FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627915` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062792B` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627958` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062797E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00627997` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006278AA` → RVA `0x00F048B8` (`.data`; read)
- `0x006278C3` → RVA `0x00F04980` (`.data`; read)
- `0x006278CF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00627830  48 8B C4                        mov rax, rsp
00627833  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00627837  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062783B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0062783F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00627843  55                              push rbp
00627844  41 54                           push r12
00627846  41 55                           push r13
00627848  41 56                           push r14
0062784A  41 57                           push r15
0062784C  48 8B EC                        mov rbp, rsp
0062784F  48 83 EC 60                     sub rsp, 0x60
00627853  0F 57 C0                        xorps xmm0, xmm0
00627856  33 C0                           xor eax, eax
00627858  B9 6F 01 00 00                  mov ecx, 0x16f
0062785D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00627861  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00627865  4D 8B F9                        mov r15, r9
00627868  45 8A E0                        mov r12b, r8b
0062786B  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0062786F  44 8A EA                        mov r13b, dl
00627872  E8 BD E1 E6 FF                  call 0x140495a34
00627877  4C 8B F0                        mov r14, rax
0062787A  48 85 C0                        test rax, rax
0062787D  0F 84 97 00 00 00               je 0x14062791a
00627883  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00627886  F6 C1 18                        test cl, 0x18
00627889  74 0A                           je 0x140627895
0062788B  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0062788F  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00627893  EB 0E                           jmp 0x1406278a3
00627895  F6 C1 04                        test cl, 4
00627898  74 09                           je 0x1406278a3
0062789A  E8 69 C3 EA FF                  call 0x1404d3c08
0062789F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
006278A3  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
006278A7  40 32 F6                        xor sil, sil
006278AA  40 38 35 07 D0 8D 00            cmp byte ptr [rip + 0x8dd007], sil
006278B1  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
006278B5  44 88 6D E1                     mov byte ptr [rbp - 0x1f], r13b
006278B9  44 88 65 E0                     mov byte ptr [rbp - 0x20], r12b
006278BD  4C 89 7D D8                     mov qword ptr [rbp - 0x28], r15
006278C1  75 0C                           jne 0x1406278cf
006278C3  F7 05 B3 D0 8D 00 00 08 00 00   test dword ptr [rip + 0x8dd0b3], 0x800
006278CD  74 13                           je 0x1406278e2
006278CF  48 8D 0D AA C5 8D 00            lea rcx, [rip + 0x8dc5aa]
006278D6  E8 45 ED BE FF                  call 0x140216620
006278DB  40 8A F0                        mov sil, al
006278DE  84 C0                           test al, al
006278E0  74 38                           je 0x14062791a
006278E2  49 8D 7E 20                     lea rdi, [r14 + 0x20]
006278E6  48 8B 1F                        mov rbx, qword ptr [rdi]
006278E9  EB 19                           jmp 0x140627904
006278EB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006278EF  48 85 C0                        test rax, rax
006278F2  74 0D                           je 0x140627901
006278F4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006278F8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
006278FC  E8 CF 31 09 00                  call 0x1406baad0
00627901  48 8B 1B                        mov rbx, qword ptr [rbx]
00627904  48 3B DF                        cmp rbx, rdi
00627907  75 E2                           jne 0x1406278eb
00627909  40 84 F6                        test sil, sil
0062790C  74 0C                           je 0x14062791a
0062790E  48 8D 0D 6B C5 8D 00            lea rcx, [rip + 0x8dc56b]
00627915  E8 66 25 D2 FF                  call 0x140349e80
0062791A  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0062791E  4D 8B CF                        mov r9, r15
00627921  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00627925  45 8A C4                        mov r8b, r12b
00627928  41 8A D5                        mov dl, r13b
0062792B  E8 A0 31 09 00                  call 0x1406baad0
00627930  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00627934  4D 85 F6                        test r14, r14
00627937  74 63                           je 0x14062799c
00627939  40 32 FF                        xor dil, dil
0062793C  40 38 3D 75 CF 8D 00            cmp byte ptr [rip + 0x8dcf75], dil
00627943  75 0C                           jne 0x140627951
00627945  F7 05 31 D0 8D 00 00 08 00 00   test dword ptr [rip + 0x8dd031], 0x800
0062794F  74 13                           je 0x140627964
00627951  48 8D 0D 28 C5 8D 00            lea rcx, [rip + 0x8dc528]
00627958  E8 C3 EC BE FF                  call 0x140216620
0062795D  40 8A F8                        mov dil, al
00627960  84 C0                           test al, al
00627962  74 38                           je 0x14062799c
00627964  49 8D 76 30                     lea rsi, [r14 + 0x30]
00627968  48 8B 1E                        mov rbx, qword ptr [rsi]
0062796B  EB 19                           jmp 0x140627986
0062796D  48 8D 43 F0                     lea rax, [rbx - 0x10]
00627971  48 85 C0                        test rax, rax
00627974  74 0D                           je 0x140627983
00627976  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062797A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0062797E  E8 4D 31 09 00                  call 0x1406baad0
00627983  48 8B 1B                        mov rbx, qword ptr [rbx]
00627986  48 3B DE                        cmp rbx, rsi
00627989  75 E2                           jne 0x14062796d
0062798B  40 84 FF                        test dil, dil
0062798E  74 0C                           je 0x14062799c
00627990  48 8D 0D E9 C4 8D 00            lea rcx, [rip + 0x8dc4e9]
00627997  E8 E4 24 D2 FF                  call 0x140349e80
0062799C  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
006279A0  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
006279A5  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
006279A9  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
006279AD  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
006279B1  49 8B E3                        mov rsp, r11
006279B4  41 5F                           pop r15
006279B6  41 5E                           pop r14
006279B8  41 5D                           pop r13
006279BA  41 5C                           pop r12
006279BC  5D                              pop rbp
006279BD  C3                              ret
006279BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoAllocateIrpExWrapper(__int64 a1, unsigned __int8 a2, unsigned __int8 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_m47;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(367, a2, a3, a4);
    if (result == 0) goto loc_0062791A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00627895;
    v_stack_m58 = v_stack_p0;
    goto loc_006278A3;
loc_00627895:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m47 = a2;
    v_stack_m48 = a3;
    v_stack_m50 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9293831)) != 0) goto loc_006278CF;
    if (((*(unsigned int *)(v_rip + 9294003)) & (0x800ULL)) == 0) goto loc_006278E2;
loc_006278CF:
    result = ExAcquireRundownProtection(v_rip + 9291178, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062791A;
loc_006278E2:
    goto loc_00627904;
loc_006278EB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00627904:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006278EB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9291115;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = guard_dispatch_icall(v_stack_p8, a2, a3, a4);
    v_stack_m38 = result;
    if (result == 0) goto loc_0062799C;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9293685)) != 0) goto loc_00627951;
    if (((*(unsigned int *)(v_rip + 9293873)) & (0x800ULL)) == 0) goto loc_00627964;
loc_00627951:
    result = ExAcquireRundownProtection(v_rip + 9291048, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062799C;
loc_00627964:
    goto loc_00627986;
loc_0062796D:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00627986:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0062796D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9290985;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoAllocateIrpExWrapper(int64_t Arg1, uint8_t Arg2, uint8_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint8_t v_stack_m47;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(367, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0062791A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00627895;
    v_stack_m58 = v_stack_p0;
    goto loc_006278A3;
loc_00627895:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m47 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m50 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8DD007)) != 0) goto loc_006278CF;
    if (((*(uint32_t *)(v_rip + 0x8DD0B3)) & (0x800ULL)) == 0) goto loc_006278E2;
loc_006278CF:
    result = ExAcquireRundownProtection(v_rip + 9291178, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062791A;
loc_006278E2:
    goto loc_00627904;
loc_006278EB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00627904:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006278EB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9291115;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = guard_dispatch_icall(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m38 = result;
    if (result == 0) goto loc_0062799C;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DCF75)) != 0) goto loc_00627951;
    if (((*(uint32_t *)(v_rip + 0x8DD031)) & (0x800ULL)) == 0) goto loc_00627964;
loc_00627951:
    result = ExAcquireRundownProtection(v_rip + 9291048, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0062799C;
loc_00627964:
    goto loc_00627986;
loc_0062796D:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00627986:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0062796D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9290985;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00627830&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00627830[BB_00627830]
  bb_00627883[BB_00627883]
  bb_0062788B[BB_0062788B]
  bb_00627895[BB_00627895]
  bb_0062789A[BB_0062789A]
  bb_006278A3[BB_006278A3]
  bb_006278C3[BB_006278C3]
  bb_006278CF[BB_006278CF]
  bb_006278E2[BB_006278E2]
  bb_006278EB[BB_006278EB]
  bb_006278F4[BB_006278F4]
  bb_00627901[BB_00627901]
  bb_00627904[BB_00627904]
  bb_00627909[BB_00627909]
  bb_0062790E[BB_0062790E]
  bb_0062791A[BB_0062791A]
  bb_00627939[BB_00627939]
  bb_00627945[BB_00627945]
  bb_00627951[BB_00627951]
  bb_00627964[BB_00627964]
  bb_0062796D[BB_0062796D]
  bb_00627976[BB_00627976]
  bb_00627983[BB_00627983]
  bb_00627986[BB_00627986]
  bb_0062798B[BB_0062798B]
  bb_00627990[BB_00627990]
  bb_0062799C[BB_0062799C]
  bb_006279BE[BB_006279BE]
  bb_00627830 -->|branch| bb_0062791A
  bb_00627830 -->|fallthrough| bb_00627883
  bb_00627883 -->|branch| bb_00627895
  bb_00627883 -->|fallthrough| bb_0062788B
  bb_0062788B -->|branch| bb_006278A3
  bb_00627895 -->|branch| bb_006278A3
  bb_00627895 -->|fallthrough| bb_0062789A
  bb_0062789A -->|flow| bb_006278A3
  bb_006278A3 -->|branch| bb_006278CF
  bb_006278A3 -->|fallthrough| bb_006278C3
  bb_006278C3 -->|branch| bb_006278E2
  bb_006278C3 -->|fallthrough| bb_006278CF
  bb_006278CF -->|branch| bb_0062791A
  bb_006278CF -->|fallthrough| bb_006278E2
  bb_006278E2 -->|branch| bb_00627904
  bb_006278EB -->|branch| bb_00627901
  bb_006278EB -->|fallthrough| bb_006278F4
  bb_006278F4 -->|flow| bb_00627901
  bb_00627901 -->|flow| bb_00627904
  bb_00627904 -->|branch| bb_006278EB
  bb_00627904 -->|fallthrough| bb_00627909
  bb_00627909 -->|branch| bb_0062791A
  bb_00627909 -->|fallthrough| bb_0062790E
  bb_0062790E -->|flow| bb_0062791A
  bb_0062791A -->|branch| bb_0062799C
  bb_0062791A -->|fallthrough| bb_00627939
  bb_00627939 -->|branch| bb_00627951
  bb_00627939 -->|fallthrough| bb_00627945
  bb_00627945 -->|branch| bb_00627964
  bb_00627945 -->|fallthrough| bb_00627951
  bb_00627951 -->|branch| bb_0062799C
  bb_00627951 -->|fallthrough| bb_00627964
  bb_00627964 -->|branch| bb_00627986
  bb_0062796D -->|branch| bb_00627983
  bb_0062796D -->|fallthrough| bb_00627976
  bb_00627976 -->|flow| bb_00627983
  bb_00627983 -->|flow| bb_00627986
  bb_00627986 -->|branch| bb_0062796D
  bb_00627986 -->|fallthrough| bb_0062798B
  bb_0062798B -->|branch| bb_0062799C
  bb_0062798B -->|fallthrough| bb_00627990
  bb_00627990 -->|flow| bb_0062799C
```
