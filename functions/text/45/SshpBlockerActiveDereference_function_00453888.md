# SshpBlockerActiveDereference

- RVA: `0x00453888`–`0x004538C2` (길이 `58` bytes)
- VA: `0x0000000140453888`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A7810`
- 디코드: `19`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004538AD` → [SshpIterateParentBlockers](SshpIterateParentBlockers_function_0045394C.md) (function, `0x0045394C`)

### Direct callers
- [SleepstudyHelperBlockerActiveDereference](SleepstudyHelperBlockerActiveDereference_function_00453830.md) at `0x00453856`
- [SshpDereferenceBlocker](../48/SshpDereferenceBlocker_function_00486960.md) at `0x00486B2B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00453888  48 8B C4                        mov rax, rsp
0045388B  53                              push rbx
0045388C  48 83 EC 40                     sub rsp, 0x40
00453890  39 51 14                        cmp dword ptr [rcx + 0x14], edx
00453893  7C 26                           jl 0x1404538bb
00453895  33 DB                           xor ebx, ebx
00453897  48 C7 40 D8 01 00 00 00         mov qword ptr [rax - 0x28], 1
0045389F  4C 8D 40 D8                     lea r8, [rax - 0x28]
004538A3  89 58 EC                        mov dword ptr [rax - 0x14], ebx
004538A6  48 89 48 E0                     mov qword ptr [rax - 0x20], rcx
004538AA  89 50 E8                        mov dword ptr [rax - 0x18], edx
004538AD  E8 9A 00 00 00                  call 0x14045394c
004538B2  8B C3                           mov eax, ebx
004538B4  48 83 C4 40                     add rsp, 0x40
004538B8  5B                              pop rbx
004538B9  C3                              ret
004538BA  CC                              int3
004538BB  BB 95 00 00 C0                  mov ebx, 0xc0000095
004538C0  EB F0                           jmp 0x1404538b2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpBlockerActiveDereference(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    if ((*(unsigned int *)(a1 + 20)) < a2) goto loc_004538BB;
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 40) = 1;
    *(unsigned int *)(v_rsp - 20) = 0;
    *(unsigned __int64 *)(v_rsp - 32) = a1;
    *(unsigned int *)(v_rsp - 24) = a2;
    result = SshpIterateParentBlockers(a1, a2, v_rsp - 40, a4);
loc_004538B2:
    v_rsp = (v_rsp) + (64);
    return 0;
loc_004538BB:
    goto loc_004538B2;
}
```

## 5. (Beta) C Style

```c
int64_t SshpBlockerActiveDereference(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    if ((*(uint32_t *)(arg1 + 0x14)) < Arg2) goto loc_004538BB;
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x28) = 1;
    *(uint32_t *)(local_rsp - 0x14) = 0;
    *(void **)(local_rsp - 0x20) = Arg1;
    *(uint32_t *)(local_rsp - 0x18) = Arg2;
    result = SshpIterateParentBlockers(Arg1, Arg2, local_rsp - 40, a4);
loc_004538B2:
    local_rsp = (local_rsp) + (64);
    return 0;
loc_004538BB:
    goto loc_004538B2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x14` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00453888&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00453888[BB_00453888]
  bb_00453895[BB_00453895]
  bb_004538B2[BB_004538B2]
  bb_004538BA[BB_004538BA]
  bb_004538BB[BB_004538BB]
  bb_00453888 -->|branch| bb_004538BB
  bb_00453888 -->|fallthrough| bb_00453895
  bb_00453895 -->|flow| bb_004538B2
  bb_004538BA -->|flow| bb_004538BB
  bb_004538BB -->|branch| bb_004538B2
```
