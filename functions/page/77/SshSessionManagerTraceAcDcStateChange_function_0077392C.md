# SshSessionManagerTraceAcDcStateChange

- RVA: `0x0077392C`–`0x007739E2` (길이 `182` bytes)
- VA: `0x000000014077392C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A288`
- 디코드: `40`개 명령, `182/182` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007739C7` → [SshpSessionManagerSendControlEvent](../A8/SshpSessionManagerSendControlEvent_function_00A871C0.md) (function, `0x00A871C0`)
- `0x007739D3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopDiagTraceAcDcStateChange](../76/PopDiagTraceAcDcStateChange_function_0076035C.md) at `0x00760445`

### Static image references
- `0x00773949` → RVA `0x00E0A740` (`.data`; read)
- `0x0077397B` → RVA `0x00029788` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007739D3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077392C  48 8B C4                        mov rax, rsp
0077392F  44 88 48 20                     mov byte ptr [rax + 0x20], r9b
00773933  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
00773937  89 50 10                        mov dword ptr [rax + 0x10], edx
0077393A  89 48 08                        mov dword ptr [rax + 8], ecx
0077393D  55                              push rbp
0077393E  48 8D 68 B1                     lea rbp, [rax - 0x4f]
00773942  48 81 EC 90 00 00 00            sub rsp, 0x90
00773949  48 8B 05 F0 6D 69 00            mov rax, qword ptr [rip + 0x696df0]
00773950  48 33 C4                        xor rax, rsp
00773953  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00773957  48 8D 45 57                     lea rax, [rbp + 0x57]
0077395B  48 C7 45 DF 04 00 00 00         mov qword ptr [rbp - 0x21], 4
00773963  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
00773967  4C 8D 45 D7                     lea r8, [rbp - 0x29]
0077396B  48 8D 45 5F                     lea rax, [rbp + 0x5f]
0077396F  48 C7 45 EF 04 00 00 00         mov qword ptr [rbp - 0x11], 4
00773977  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0077397B  48 8D 0D 06 5E 8B FF            lea rcx, [rip - 0x74a1fa]
00773982  48 8D 45 67                     lea rax, [rbp + 0x67]
00773986  48 C7 45 FF 04 00 00 00         mov qword ptr [rbp - 1], 4
0077398E  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00773992  BA 06 00 00 00                  mov edx, 6
00773997  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0077399B  48 C7 45 0F 01 00 00 00         mov qword ptr [rbp + 0xf], 1
007739A3  48 89 45 07                     mov qword ptr [rbp + 7], rax
007739A7  48 8D 45 77                     lea rax, [rbp + 0x77]
007739AB  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007739AF  48 8D 45 7F                     lea rax, [rbp + 0x7f]
007739B3  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007739B7  48 C7 45 1F 01 00 00 00         mov qword ptr [rbp + 0x1f], 1
007739BF  48 C7 45 2F 01 00 00 00         mov qword ptr [rbp + 0x2f], 1
007739C7  E8 F4 37 31 00                  call 0x140a871c0
007739CC  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
007739D0  48 33 CC                        xor rcx, rsp
007739D3  E8 68 8C F3 FF                  call 0x1406ac640
007739D8  48 81 C4 90 00 00 00            add rsp, 0x90
007739DF  5D                              pop rbp
007739E0  C3                              ret
007739E1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshSessionManagerTraceAcDcStateChange(int a1, int a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rsp;

    *(unsigned __int8 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned int *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 6909424)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 79 + 55) = result;
    *(unsigned __int64 *)(v_rsp - 79 - 33) = 4;
    *(unsigned __int64 *)(v_rsp - 79 - 41) = v_rsp - 79 + 87;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = 4;
    *(unsigned __int64 *)(v_rsp - 79 - 25) = v_rsp - 79 + 95;
    *(unsigned __int64 *)(v_rsp - 79 - 1) = 4;
    *(unsigned __int64 *)(v_rsp - 79 - 9) = v_rsp - 79 + 103;
    *(unsigned __int64 *)(v_rsp - 79 + 15) = 1;
    *(unsigned __int64 *)(v_rsp - 79 + 7) = v_rsp - 79 + 111;
    *(unsigned __int64 *)(v_rsp - 79 + 23) = v_rsp - 79 + 119;
    *(unsigned __int64 *)(v_rsp - 79 + 39) = v_rsp - 79 + 127;
    *(unsigned __int64 *)(v_rsp - 79 + 31) = 1;
    *(unsigned __int64 *)(v_rsp - 79 + 47) = 1;
    result = SshpSessionManagerSendControlEvent(v_rip - 7643642, 6, v_rsp - 79 - 41, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 79 + 55)) ^ (v_rsp);
    result = _security_check_cookie(a1, 6, v_rsp - 79 - 41, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SshSessionManagerTraceAcDcStateChange(int32_t Arg1, int32_t Arg2, int32_t Arg3, uint8_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    *(uint8_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(uint32_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x696DF0)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x4F + 0x37) = result;
    *(uint64_t *)(local_rsp - 0x4F - 0x21) = 4;
    *(uint64_t *)(local_rsp - 0x4F - 0x29) = local_rsp - 79 + 87;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = 4;
    *(uint64_t *)(local_rsp - 0x4F - 0x19) = local_rsp - 79 + 95;
    *(uint64_t *)(local_rsp - 0x4F - 0x1) = 4;
    *(uint64_t *)(local_rsp - 0x4F - 0x9) = local_rsp - 79 + 103;
    *(uint64_t *)(local_rsp - 0x4F + 0xF) = 1;
    *(uint64_t *)(local_rsp - 0x4F + 0x7) = local_rsp - 79 + 111;
    *(uint64_t *)(local_rsp - 0x4F + 0x17) = local_rsp - 79 + 119;
    *(uint64_t *)(local_rsp - 0x4F + 0x27) = local_rsp - 79 + 127;
    *(uint64_t *)(local_rsp - 0x4F + 0x1F) = 1;
    *(uint64_t *)(local_rsp - 0x4F + 0x2F) = 1;
    result = SshpSessionManagerSendControlEvent(v_rip - 7643642, 6, local_rsp - 79 - 41, Arg4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x4F + 0x37)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 6, local_rsp - 79 - 41, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077392C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077392C[BB_0077392C]
  bb_007739E1[BB_007739E1]
```
