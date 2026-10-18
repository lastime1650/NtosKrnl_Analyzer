# DifKeTryToAcquireGuardedMutexWrapper

- RVA: `0x00632F40`–`0x0063309F` (길이 `351` bytes)
- VA: `0x0000000140632F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00632F6F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00632F97` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00632FC5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00632FEC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00633005` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063300D` → [ExTryToAcquireFastMutex](../44/ExTryToAcquireFastMutex_function_0044C2E0.md) (function, `0x0044C2E0`)
- `0x0063303A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00633061` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063307A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00632FA9` → RVA `0x00F048B8` (`.data`; read)
- `0x00632FB2` → RVA `0x00F04980` (`.data`; read)
- `0x00632FBE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00632F40  4C 8B DC                        mov r11, rsp
00632F43  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00632F47  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00632F4B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00632F4F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00632F53  41 56                           push r14
00632F55  48 83 EC 40                     sub rsp, 0x40
00632F59  33 C0                           xor eax, eax
00632F5B  0F 57 C0                        xorps xmm0, xmm0
00632F5E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00632F63  48 8B E9                        mov rbp, rcx
00632F66  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00632F6A  B9 F5 00 00 00                  mov ecx, 0xf5
00632F6F  E8 C0 2A E6 FF                  call 0x140495a34
00632F74  48 8B F0                        mov rsi, rax
00632F77  48 85 C0                        test rax, rax
00632F7A  0F 84 8A 00 00 00               je 0x14063300a
00632F80  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00632F83  A8 18                           test al, 0x18
00632F85  74 0C                           je 0x140632f93
00632F87  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00632F8C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00632F91  EB 0E                           jmp 0x140632fa1
00632F93  A8 04                           test al, 4
00632F95  74 0A                           je 0x140632fa1
00632F97  E8 6C 0C EA FF                  call 0x1404d3c08
00632F9C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00632FA1  40 32 FF                        xor dil, dil
00632FA4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00632FA9  40 38 3D 08 19 8D 00            cmp byte ptr [rip + 0x8d1908], dil
00632FB0  75 0C                           jne 0x140632fbe
00632FB2  F7 05 C4 19 8D 00 00 08 00 00   test dword ptr [rip + 0x8d19c4], 0x800
00632FBC  74 13                           je 0x140632fd1
00632FBE  48 8D 0D BB 0E 8D 00            lea rcx, [rip + 0x8d0ebb]
00632FC5  E8 56 36 BE FF                  call 0x140216620
00632FCA  40 8A F8                        mov dil, al
00632FCD  84 C0                           test al, al
00632FCF  74 39                           je 0x14063300a
00632FD1  4C 8D 76 20                     lea r14, [rsi + 0x20]
00632FD5  49 8B 1E                        mov rbx, qword ptr [r14]
00632FD8  EB 1A                           jmp 0x140632ff4
00632FDA  48 8D 43 F0                     lea rax, [rbx - 0x10]
00632FDE  48 85 C0                        test rax, rax
00632FE1  74 0E                           je 0x140632ff1
00632FE3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00632FE7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00632FEC  E8 DF 7A 08 00                  call 0x1406baad0
00632FF1  48 8B 1B                        mov rbx, qword ptr [rbx]
00632FF4  49 3B DE                        cmp rbx, r14
00632FF7  75 E1                           jne 0x140632fda
00632FF9  40 84 FF                        test dil, dil
00632FFC  74 0C                           je 0x14063300a
00632FFE  48 8D 0D 7B 0E 8D 00            lea rcx, [rip + 0x8d0e7b]
00633005  E8 76 6E D1 FF                  call 0x140349e80
0063300A  48 8B CD                        mov rcx, rbp
0063300D  E8 CE 92 E1 FF                  call 0x14044c2e0
00633012  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00633016  48 85 F6                        test rsi, rsi
00633019  74 64                           je 0x14063307f
0063301B  40 32 FF                        xor dil, dil
0063301E  40 38 3D 93 18 8D 00            cmp byte ptr [rip + 0x8d1893], dil
00633025  75 0C                           jne 0x140633033
00633027  F7 05 4F 19 8D 00 00 08 00 00   test dword ptr [rip + 0x8d194f], 0x800
00633031  74 13                           je 0x140633046
00633033  48 8D 0D 46 0E 8D 00            lea rcx, [rip + 0x8d0e46]
0063303A  E8 E1 35 BE FF                  call 0x140216620
0063303F  40 8A F8                        mov dil, al
00633042  84 C0                           test al, al
00633044  74 39                           je 0x14063307f
00633046  48 83 C6 30                     add rsi, 0x30
0063304A  48 8B 1E                        mov rbx, qword ptr [rsi]
0063304D  EB 1A                           jmp 0x140633069
0063304F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00633053  48 85 C0                        test rax, rax
00633056  74 0E                           je 0x140633066
00633058  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063305C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00633061  E8 6A 7A 08 00                  call 0x1406baad0
00633066  48 8B 1B                        mov rbx, qword ptr [rbx]
00633069  48 3B DE                        cmp rbx, rsi
0063306C  75 E1                           jne 0x14063304f
0063306E  40 84 FF                        test dil, dil
00633071  74 0C                           je 0x14063307f
00633073  48 8D 0D 06 0E 8D 00            lea rcx, [rip + 0x8d0e06]
0063307A  E8 01 6E D1 FF                  call 0x140349e80
0063307F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00633083  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00633088  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063308D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00633092  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00633097  48 83 C4 40                     add rsp, 0x40
0063309B  41 5E                           pop r14
0063309D  C3                              ret
0063309E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifKeTryToAcquireGuardedMutexWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(245, a2, a3, a4);
    if (result == 0) goto loc_0063300A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00632F93;
    v_stack_m28 = v_stack_p0;
    goto loc_00632FA1;
loc_00632F93:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9246984)) != 0) goto loc_00632FBE;
    if (((*(unsigned int *)(v_rip + 9247172)) & (0x800ULL)) == 0) goto loc_00632FD1;
loc_00632FBE:
    result = ExAcquireRundownProtection(v_rip + 9244347, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063300A;
loc_00632FD1:
    goto loc_00632FF4;
loc_00632FDA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00632FF4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00632FDA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9244283;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExTryToAcquireFastMutex(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0063307F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9246867)) != 0) goto loc_00633033;
    if (((*(unsigned int *)(v_rip + 9247055)) & (0x800ULL)) == 0) goto loc_00633046;
loc_00633033:
    result = ExAcquireRundownProtection(v_rip + 9244230, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063307F;
loc_00633046:
    v_rsi = (result) + (48);
    goto loc_00633069;
loc_0063304F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00633069:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063304F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9244166;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifKeTryToAcquireGuardedMutexWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(245, a2, a3, a4);
    if (result == 0) goto loc_0063300A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00632F93;
    v_stack_m28 = v_stack_p0;
    goto loc_00632FA1;
loc_00632F93:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D1908)) != 0) goto loc_00632FBE;
    if (((*(uint32_t *)(v_rip + 0x8D19C4)) & (0x800ULL)) == 0) goto loc_00632FD1;
loc_00632FBE:
    result = ExAcquireRundownProtection(v_rip + 9244347, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063300A;
loc_00632FD1:
    goto loc_00632FF4;
loc_00632FDA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00632FF4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00632FDA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9244283;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExTryToAcquireFastMutex(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0063307F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D1893)) != 0) goto loc_00633033;
    if (((*(uint32_t *)(v_rip + 0x8D194F)) & (0x800ULL)) == 0) goto loc_00633046;
loc_00633033:
    result = ExAcquireRundownProtection(v_rip + 9244230, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063307F;
loc_00633046:
    local_rsi = (result) + (48);
    goto loc_00633069;
loc_0063304F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00633069:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063304F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9244166;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00632F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00632F40[BB_00632F40]
  bb_00632F80[BB_00632F80]
  bb_00632F87[BB_00632F87]
  bb_00632F93[BB_00632F93]
  bb_00632F97[BB_00632F97]
  bb_00632FA1[BB_00632FA1]
  bb_00632FB2[BB_00632FB2]
  bb_00632FBE[BB_00632FBE]
  bb_00632FD1[BB_00632FD1]
  bb_00632FDA[BB_00632FDA]
  bb_00632FE3[BB_00632FE3]
  bb_00632FF1[BB_00632FF1]
  bb_00632FF4[BB_00632FF4]
  bb_00632FF9[BB_00632FF9]
  bb_00632FFE[BB_00632FFE]
  bb_0063300A[BB_0063300A]
  bb_0063301B[BB_0063301B]
  bb_00633027[BB_00633027]
  bb_00633033[BB_00633033]
  bb_00633046[BB_00633046]
  bb_0063304F[BB_0063304F]
  bb_00633058[BB_00633058]
  bb_00633066[BB_00633066]
  bb_00633069[BB_00633069]
  bb_0063306E[BB_0063306E]
  bb_00633073[BB_00633073]
  bb_0063307F[BB_0063307F]
  bb_0063309E[BB_0063309E]
  bb_00632F40 -->|branch| bb_0063300A
  bb_00632F40 -->|fallthrough| bb_00632F80
  bb_00632F80 -->|branch| bb_00632F93
  bb_00632F80 -->|fallthrough| bb_00632F87
  bb_00632F87 -->|branch| bb_00632FA1
  bb_00632F93 -->|branch| bb_00632FA1
  bb_00632F93 -->|fallthrough| bb_00632F97
  bb_00632F97 -->|flow| bb_00632FA1
  bb_00632FA1 -->|branch| bb_00632FBE
  bb_00632FA1 -->|fallthrough| bb_00632FB2
  bb_00632FB2 -->|branch| bb_00632FD1
  bb_00632FB2 -->|fallthrough| bb_00632FBE
  bb_00632FBE -->|branch| bb_0063300A
  bb_00632FBE -->|fallthrough| bb_00632FD1
  bb_00632FD1 -->|branch| bb_00632FF4
  bb_00632FDA -->|branch| bb_00632FF1
  bb_00632FDA -->|fallthrough| bb_00632FE3
  bb_00632FE3 -->|flow| bb_00632FF1
  bb_00632FF1 -->|flow| bb_00632FF4
  bb_00632FF4 -->|branch| bb_00632FDA
  bb_00632FF4 -->|fallthrough| bb_00632FF9
  bb_00632FF9 -->|branch| bb_0063300A
  bb_00632FF9 -->|fallthrough| bb_00632FFE
  bb_00632FFE -->|flow| bb_0063300A
  bb_0063300A -->|branch| bb_0063307F
  bb_0063300A -->|fallthrough| bb_0063301B
  bb_0063301B -->|branch| bb_00633033
  bb_0063301B -->|fallthrough| bb_00633027
  bb_00633027 -->|branch| bb_00633046
  bb_00633027 -->|fallthrough| bb_00633033
  bb_00633033 -->|branch| bb_0063307F
  bb_00633033 -->|fallthrough| bb_00633046
  bb_00633046 -->|branch| bb_00633069
  bb_0063304F -->|branch| bb_00633066
  bb_0063304F -->|fallthrough| bb_00633058
  bb_00633058 -->|flow| bb_00633066
  bb_00633066 -->|flow| bb_00633069
  bb_00633069 -->|branch| bb_0063304F
  bb_00633069 -->|fallthrough| bb_0063306E
  bb_0063306E -->|branch| bb_0063307F
  bb_0063306E -->|fallthrough| bb_00633073
  bb_00633073 -->|flow| bb_0063307F
```
