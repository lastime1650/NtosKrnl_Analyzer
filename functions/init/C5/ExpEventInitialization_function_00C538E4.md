# ExpEventInitialization

- RVA: `0x00C538E4`–`0x00C5399B` (길이 `183` bytes)
- VA: `0x0000000140C538E4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C43B4`
- 디코드: `40`개 명령, `183/183` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C53916` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C53929` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C53973` → [ObCreateObjectType](../../page/70/ObCreateObjectType_function_00705230.md) (function, `0x00705230`)
- `0x00C53984` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExpInitSystemPhase1](ExpInitSystemPhase1_function_00C51508.md) at `0x00C515C5`

### Static image references
- `0x00C538F6` → RVA `0x00E0A740` (`.data`; read)
- `0x00C53907` → RVA `0x00C7DDF0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C5392E` → RVA `0x00C82530` (`ExpEventMapping`; read)
- `0x00C53935` → RVA `0x00FC6B80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x00C53916` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C53929` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C53973` → [ObCreateObjectType](../../page/70/ObCreateObjectType_function_00705230.md) (`INIT` → `PAGE`)
  - `0x00C53984` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C538E4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C538E9  55                              push rbp
00C538EA  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00C538EF  48 81 EC C0 00 00 00            sub rsp, 0xc0
00C538F6  48 8B 05 43 6E 1B 00            mov rax, qword ptr [rip + 0x1b6e43]
00C538FD  48 33 C4                        xor rax, rsp
00C53900  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00C53904  0F 57 C0                        xorps xmm0, xmm0
00C53907  48 8D 15 E2 A4 02 00            lea rdx, [rip + 0x2a4e2]
00C5390E  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00C53912  0F 11 45 B7                     movups xmmword ptr [rbp - 0x49], xmm0
00C53916  E8 65 6E 7D FF                  call 0x14042a780
00C5391B  BB 78 00 00 00                  mov ebx, 0x78
00C53920  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00C53924  44 8B C3                        mov r8d, ebx
00C53927  33 D2                           xor edx, edx
00C53929  E8 12 33 A7 FF                  call 0x1406c6c40
00C5392E  0F 10 05 FB EB 02 00            movups xmm0, xmmword ptr [rip + 0x2ebfb]
00C53935  4C 8D 0D 44 32 37 00            lea r9, [rip + 0x373244]
00C5393C  66 89 5D C7                     mov word ptr [rbp - 0x39], bx
00C53940  45 33 C0                        xor r8d, r8d
00C53943  C7 45 CB 10 00 00 00            mov dword ptr [rbp - 0x35], 0x10
00C5394A  48 8D 55 C7                     lea rdx, [rbp - 0x39]
00C5394E  C7 45 CF 00 01 00 00            mov dword ptr [rbp - 0x31], 0x100
00C53955  48 8D 4D B7                     lea rcx, [rbp - 0x49]
00C53959  C7 45 EB 00 02 00 00            mov dword ptr [rbp - 0x15], 0x200
00C53960  F3 0F 7F 45 D3                  movdqu xmmword ptr [rbp - 0x2d], xmm0
00C53965  C7 45 F3 18 00 00 00            mov dword ptr [rbp - 0xd], 0x18
00C5396C  C7 45 E3 03 00 1F 00            mov dword ptr [rbp - 0x1d], 0x1f0003
00C53973  E8 B8 18 AB FF                  call 0x140705230
00C53978  C1 E8 1F                        shr eax, 0x1f
00C5397B  34 01                           xor al, 1
00C5397D  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00C53981  48 33 CC                        xor rcx, rsp
00C53984  E8 B7 8C A5 FF                  call 0x1406ac640
00C53989  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00C53991  48 81 C4 C0 00 00 00            add rsp, 0xc0
00C53998  5D                              pop rbp
00C53999  C3                              ret
00C5399A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpEventInitialization(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m74;
    unsigned int v_stack_m7C;
    unsigned __int64 v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 1797699)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_mA8 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mA8, v_rip + 173282, a3, a4);
    a2 = 0;
    result = memset(v_stack_m98, a2, 120, a4);
    v_stack_m98 = 120;
    a3 = 0;
    v_stack_m94 = 16;
    v_stack_m90 = 256;
    v_stack_m74 = 512;
    v_stack_m8C = v_xmm0;
    v_stack_m6C = 24;
    v_stack_m7C = 0x1F0003ULL;
    result = ObCreateObjectType(v_stack_mA8, v_stack_m98, a3, v_rip + 3617348);
    result = (unsigned int)((result) >> (31));
    result = (unsigned __int8)((result) ^ (1));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m98, a3, v_rip + 3617348);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
void ExpEventInitialization(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m74;
    uint32_t v_stack_m7C;
    uint64_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x1B6E43)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_mA8 = v_xmm0;
    result = RtlInitUnicodeString(v_stack_mA8, v_rip + 173282, a3, a4);
    a2 = 0;
    result = memset(v_stack_m98, a2, 120, a4);
    v_stack_m98 = 120;
    a3 = 0;
    v_stack_m94 = 16;
    v_stack_m90 = 256;
    v_stack_m74 = 512;
    v_stack_m8C = v_xmm0;
    v_stack_m6C = 24;
    v_stack_m7C = 0x1F0003ULL;
    result = ObCreateObjectType(v_stack_mA8, v_stack_m98, a3, v_rip + 3617348);
    result = (uint32_t)((result) >> (31));
    result = (uint8_t)((result) ^ (1));
    a1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(a1, v_stack_m98, a3, v_rip + 3617348);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C538E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C538E4[BB_00C538E4]
  bb_00C5399A[BB_00C5399A]
```
