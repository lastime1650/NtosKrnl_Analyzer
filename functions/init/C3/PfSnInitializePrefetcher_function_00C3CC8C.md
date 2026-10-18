# PfSnInitializePrefetcher

- RVA: `0x00C3CC8C`–`0x00C3CE04` (길이 `376` bytes)
- VA: `0x0000000140C3CC8C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000697A4`
- 디코드: `73`개 명령, `376/376` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **27**

### Outgoing calls
- `0x00C3CD21` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C3CD35` → [PfpCreateEvent](../../page/75/PfpCreateEvent_function_00753460.md) (function, `0x00753460`)
- `0x00C3CD41` → [PfSnPrefetchCacheCtxInitialize](../../page/75/PfSnPrefetchCacheCtxInitialize_function_007523E8.md) (function, `0x007523E8`)
- `0x00C3CD5B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00C3CDD6` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (function, `0x00232CB0`)

### Direct callers
- [PfInitializeSuperfetch](PfInitializeSuperfetch_function_00C3CACC.md) at `0x00C3CBF7`

### Static image references
- `0x00C3CC94` → RVA `0x00E67278` (`.data`; write)
- `0x00C3CC9E` → RVA `0x00E67250` (`.data`; read)
- `0x00C3CCA5` → RVA `0x00E67260` (`.data`; write)
- `0x00C3CCAC` → RVA `0x00E67258` (`.data`; write)
- `0x00C3CCB3` → RVA `0x00C7BD70` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C3CCBA` → RVA `0x00E67250` (`.data`; write)
- `0x00C3CCC6` → RVA `0x00E67268` (`.data`; read)
- `0x00C3CCCD` → RVA `0x00E67280` (`.data`; write)
- `0x00C3CCD4` → RVA `0x00E67270` (`.data`; write)
- `0x00C3CCDE` → RVA `0x00E67268` (`.data`; write)
- `0x00C3CCE5` → RVA `0x00E67298` (`.data`; read)
- `0x00C3CCEC` → RVA `0x00E672A0` (`.data`; write)
- `0x00C3CCF3` → RVA `0x00E67298` (`.data`; write)
- `0x00C3CCFF` → RVA `0x00E67288` (`.data`; write)
- `0x00C3CD05` → RVA `0x00E67290` (`.data`; write)
- `0x00C3CD0E` → RVA `0x00E67292` (`.data`; write)
- `0x00C3CD15` → RVA `0x00E67294` (`.data`; write)
- `0x00C3CD1B` → RVA `0x00E672B4` (`.data`; write)
- `0x00C3CD26` → RVA `0x00E672B8` (`.data`; read)
- `0x00C3CD3A` → RVA `0x00E672C8` (`.data`; read)
- `0x00C3CD4B` → RVA `0x00E67358` (`.data`; write)
- `0x00C3CD6F` → RVA `0x00582920` (`FsRtlpOplockAckTimeoutDpc`; read)
- `0x00C3CD96` → RVA `0x007528B0` (`PfSnTracingStateExWorkerRoutine`; read)
- `0x00C3CDDE` → RVA `0x00E67368` (`.data`; write)
- `0x00C3CDE5` → RVA `0x00E67370` (`.data`; write)
- `0x00C3CDEF` → RVA `0x00E67380` (`.data`; write)
- `0x00C3CDF6` → RVA `0x00E67388` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00C3CD21` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C3CD35` → [PfpCreateEvent](../../page/75/PfpCreateEvent_function_00753460.md) (`INIT` → `PAGE`)
  - `0x00C3CD41` → [PfSnPrefetchCacheCtxInitialize](../../page/75/PfSnPrefetchCacheCtxInitialize_function_007523E8.md) (`INIT` → `PAGE`)
  - `0x00C3CD5B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`INIT` → `POOLCODE`)
  - `0x00C3CDD6` → [KiSetTimerEx](../../text/23/KiSetTimerEx_function_00232CB0.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3CC8C  40 53                           push rbx
00C3CC8E  48 83 EC 40                     sub rsp, 0x40
00C3CC92  33 DB                           xor ebx, ebx
00C3CC94  C7 05 DA A5 22 00 01 00 00 00   mov dword ptr [rip + 0x22a5da], 1
00C3CC9E  48 8D 05 AB A5 22 00            lea rax, [rip + 0x22a5ab]
00C3CCA5  48 89 1D B4 A5 22 00            mov qword ptr [rip + 0x22a5b4], rbx
00C3CCAC  48 89 05 A5 A5 22 00            mov qword ptr [rip + 0x22a5a5], rax
00C3CCB3  48 8D 15 B6 F0 03 00            lea rdx, [rip + 0x3f0b6]
00C3CCBA  48 89 05 8F A5 22 00            mov qword ptr [rip + 0x22a58f], rax
00C3CCC1  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00C3CCC6  48 8D 05 9B A5 22 00            lea rax, [rip + 0x22a59b]
00C3CCCD  48 89 1D AC A5 22 00            mov qword ptr [rip + 0x22a5ac], rbx
00C3CCD4  48 89 05 95 A5 22 00            mov qword ptr [rip + 0x22a595], rax
00C3CCDB  0F 57 C0                        xorps xmm0, xmm0
00C3CCDE  48 89 05 83 A5 22 00            mov qword ptr [rip + 0x22a583], rax
00C3CCE5  48 8D 05 AC A5 22 00            lea rax, [rip + 0x22a5ac]
00C3CCEC  48 89 05 AD A5 22 00            mov qword ptr [rip + 0x22a5ad], rax
00C3CCF3  48 89 05 9E A5 22 00            mov qword ptr [rip + 0x22a59e], rax
00C3CCFA  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
00C3CCFF  89 1D 83 A5 22 00               mov dword ptr [rip + 0x22a583], ebx
00C3CD05  66 C7 05 82 A5 22 00 01 00      mov word ptr [rip + 0x22a582], 1
00C3CD0E  C6 05 7D A5 22 00 06            mov byte ptr [rip + 0x22a57d], 6
00C3CD15  89 1D 79 A5 22 00               mov dword ptr [rip + 0x22a579], ebx
00C3CD1B  89 1D 93 A5 22 00               mov dword ptr [rip + 0x22a593], ebx
00C3CD21  E8 5A DA 7E FF                  call 0x14042a780
00C3CD26  4C 8D 05 8B A5 22 00            lea r8, [rip + 0x22a58b]
00C3CD2D  8D 53 01                        lea edx, [rbx + 1]
00C3CD30  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00C3CD35  E8 26 67 B1 FF                  call 0x140753460
00C3CD3A  48 8D 0D 87 A5 22 00            lea rcx, [rip + 0x22a587]
00C3CD41  E8 A2 56 B1 FF                  call 0x1407523e8
00C3CD46  BA A0 00 00 00                  mov edx, 0xa0
00C3CD4B  48 89 1D 06 A6 22 00            mov qword ptr [rip + 0x22a606], rbx
00C3CD52  8D 4B 40                        lea ecx, [rbx + 0x40]
00C3CD55  41 B8 43 63 50 66               mov r8d, 0x66506343
00C3CD5B  E8 90 53 F4 FF                  call 0x140b820f0
00C3CD60  48 85 C0                        test rax, rax
00C3CD63  74 76                           je 0x140c3cddb
00C3CD65  48 89 18                        mov qword ptr [rax], rbx
00C3CD68  48 8D 48 08                     lea rcx, [rax + 8]
00C3CD6C  C6 00 08                        mov byte ptr [rax], 8
00C3CD6F  48 8D 15 AA 5B 94 FF            lea rdx, [rip - 0x6ba456]
00C3CD76  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00C3CD7A  45 33 C9                        xor r9d, r9d
00C3CD7D  48 89 09                        mov qword ptr [rcx], rcx
00C3CD80  45 33 C0                        xor r8d, r8d
00C3CD83  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
00C3CD87  48 8D 48 40                     lea rcx, [rax + 0x40]
00C3CD8B  89 58 3C                        mov dword ptr [rax + 0x3c], ebx
00C3CD8E  66 89 58 38                     mov word ptr [rax + 0x38], bx
00C3CD92  48 89 51 18                     mov qword ptr [rcx + 0x18], rdx
00C3CD96  48 8D 15 13 5B B1 FF            lea rdx, [rip - 0x4ea4ed]
00C3CD9D  C7 01 13 01 00 00               mov dword ptr [rcx], 0x113
00C3CDA3  48 89 41 20                     mov qword ptr [rcx + 0x20], rax
00C3CDA7  48 89 59 38                     mov qword ptr [rcx + 0x38], rbx
00C3CDAB  48 89 59 10                     mov qword ptr [rcx + 0x10], rbx
00C3CDAF  48 89 90 90 00 00 00            mov qword ptr [rax + 0x90], rdx
00C3CDB6  48 BA 00 44 5F 9A FE FF FF FF   movabs rdx, 0xfffffffe9a5f4400
00C3CDC0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C3CDC5  48 8B C8                        mov rcx, rax
00C3CDC8  48 89 80 98 00 00 00            mov qword ptr [rax + 0x98], rax
00C3CDCF  48 89 98 80 00 00 00            mov qword ptr [rax + 0x80], rbx
00C3CDD6  E8 D5 5E 5F FF                  call 0x140232cb0
00C3CDDB  0F 57 C0                        xorps xmm0, xmm0
00C3CDDE  48 89 1D 83 A5 22 00            mov qword ptr [rip + 0x22a583], rbx
00C3CDE5  66 0F 7F 05 83 A5 22 00         movdqa xmmword ptr [rip + 0x22a583], xmm0
00C3CDED  33 C0                           xor eax, eax
00C3CDEF  48 89 1D 8A A5 22 00            mov qword ptr [rip + 0x22a58a], rbx
00C3CDF6  48 89 1D 8B A5 22 00            mov qword ptr [rip + 0x22a58b], rbx
00C3CDFD  48 83 C4 40                     add rsp, 0x40
00C3CE01  5B                              pop rbx
00C3CE02  C3                              ret
00C3CE03  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnInitializePrefetcher(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (64);
    v_rbx = 0;
    *(unsigned int *)(v_rip + 2270682) = 1;
    *(unsigned __int64 *)(v_rip + 2270644) = 0;
    *(unsigned __int64 *)(v_rip + 2270629) = v_rip + 2270635;
    *(unsigned __int64 *)(v_rip + 2270607) = v_rip + 2270635;
    *(unsigned __int64 *)(v_rip + 2270636) = 0;
    *(unsigned __int64 *)(v_rip + 2270613) = v_rip + 2270619;
    *(unsigned __int64 *)(v_rip + 2270595) = v_rip + 2270619;
    *(unsigned __int64 *)(v_rip + 2270637) = v_rip + 2270636;
    *(unsigned __int64 *)(v_rip + 2270622) = v_rip + 2270636;
    v_stack_m18 = v_xmm0;
    *(unsigned int *)(v_rip + 2270595) = 0;
    *(unsigned __int16 *)(v_rip + 2270594) = 1;
    *(unsigned __int8 *)(v_rip + 2270589) = 6;
    *(unsigned int *)(v_rip + 2270585) = 0;
    *(unsigned int *)(v_rip + 2270611) = 0;
    result = RtlInitUnicodeString(v_stack_m18, v_rip + 258230, a3, a4);
    result = PfpCreateEvent(v_stack_m18, v_rbx + 1, v_rip + 2270603, a4);
    result = PfSnPrefetchCacheCtxInitialize(v_rip + 2270599, v_rbx + 1, v_rip + 2270603, a4);
    *(unsigned __int64 *)(v_rip + 2270726) = 0;
    result = ExAllocatePool2(v_rbx + 64, 160, (unsigned int)(0x66506343ULL), a4);
    if (result != 0) {
        *(unsigned __int64 *)(result) = 0;
        a1 = result + 8;
        *(unsigned __int8 *)(result) = 8;
        a2 = v_rip - 7054422;
        *(unsigned __int64 *)(a1 + 8) = a1;
        a4 = 0;
        *(unsigned __int64 *)(a1) = a1;
        a3 = 0;
        *(unsigned __int64 *)(result + 24) = 0;
        a1 = result + 64;
        *(unsigned int *)(result + 60) = 0;
        *(unsigned __int16 *)(result + 56) = 0;
        *(unsigned __int64 *)(a1 + 24) = a2;
        a2 = v_rip - 5154029;
        *(unsigned int *)(a1) = 275;
        *(unsigned __int64 *)(a1 + 32) = result;
        *(unsigned __int64 *)(a1 + 56) = 0;
        *(unsigned __int64 *)(a1 + 16) = 0;
        *(unsigned __int64 *)(result + 144) = a2;
        v_stack_m28 = a1;
        a1 = result;
        *(unsigned __int64 *)(result + 152) = result;
        *(unsigned __int64 *)(result + 128) = 0;
        result = KiSetTimerEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 2270595) = 0;
    *(unsigned __int64 *)(v_rip + 2270595) = v_xmm0;
    result = 0;
    *(unsigned __int64 *)(v_rip + 2270602) = 0;
    *(unsigned __int64 *)(v_rip + 2270603) = 0;
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnInitializePrefetcher(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (64);
    local_rbx = 0;
    *(uint32_t *)(v_rip + 0x22A5DA) = 1;
    *(uint64_t *)(v_rip + 0x22A5B4) = 0;
    *(uint64_t *)(v_rip + 0x22A5A5) = v_rip + 2270635;
    *(uint64_t *)(v_rip + 0x22A58F) = v_rip + 2270635;
    *(uint64_t *)(v_rip + 0x22A5AC) = 0;
    *(uint64_t *)(v_rip + 0x22A595) = v_rip + 2270619;
    *(uint64_t *)(v_rip + 0x22A583) = v_rip + 2270619;
    *(uint64_t *)(v_rip + 0x22A5AD) = v_rip + 2270636;
    *(uint64_t *)(v_rip + 0x22A59E) = v_rip + 2270636;
    v_stack_m18 = v_xmm0;
    *(uint32_t *)(v_rip + 0x22A583) = 0;
    *(uint16_t *)(v_rip + 0x22A582) = 1;
    *(uint8_t *)(v_rip + 0x22A57D) = 6;
    *(uint32_t *)(v_rip + 0x22A579) = 0;
    *(uint32_t *)(v_rip + 0x22A593) = 0;
    result = RtlInitUnicodeString(v_stack_m18, v_rip + 258230, Arg3, Arg4);
    result = PfpCreateEvent(v_stack_m18, local_rbx + 1, v_rip + 2270603, Arg4);
    result = PfSnPrefetchCacheCtxInitialize(v_rip + 2270599, local_rbx + 1, v_rip + 2270603, Arg4);
    *(uint64_t *)(v_rip + 0x22A606) = 0;
    result = ExAllocatePool2(local_rbx + 64, 160, (uint32_t)(0x66506343ULL), Arg4);
    if (result != 0) {
        *(uint64_t *)(result) = 0;
        Arg1 = result + 8;
        *(uint8_t *)(result) = 8;
        Arg2 = v_rip - 7054422;
        *(uint64_t *)(Arg1 + 0x8) = Arg1;
        Arg4 = 0;
        *(uint64_t *)(Arg1) = Arg1;
        Arg3 = 0;
        *(uint64_t *)(result + 0x18) = 0;
        Arg1 = result + 64;
        *(uint32_t *)(result + 0x3C) = 0;
        *(uint16_t *)(result + 0x38) = 0;
        *(uint64_t *)(Arg1 + 0x18) = Arg2;
        Arg2 = v_rip - 5154029;
        *(uint32_t *)(Arg1) = 275;
        *(uint64_t *)(Arg1 + 0x20) = result;
        *(uint64_t *)(Arg1 + 0x38) = 0;
        *(uint64_t *)(Arg1 + 0x10) = 0;
        *(uint64_t *)(result + 0x90) = Arg2;
        v_stack_m28 = Arg1;
        Arg1 = result;
        *(uint64_t *)(result + 0x98) = result;
        *(uint64_t *)(result + 0x80) = 0;
        result = KiSetTimerEx(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_rip + 0x22A583) = 0;
    *(uint64_t *)(v_rip + 0x22A583) = v_xmm0;
    result = 0;
    *(uint64_t *)(v_rip + 0x22A58A) = 0;
    *(uint64_t *)(v_rip + 0x22A58B) = 0;
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3CC8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C3CC8C[BB_00C3CC8C]
  bb_00C3CD65[BB_00C3CD65]
  bb_00C3CDDB[BB_00C3CDDB]
  bb_00C3CE03[BB_00C3CE03]
  bb_00C3CC8C -->|branch| bb_00C3CDDB
  bb_00C3CC8C -->|fallthrough| bb_00C3CD65
  bb_00C3CD65 -->|flow| bb_00C3CDDB
```
