# PspLockJobListExclusive

- RVA: `0x00917780`–`0x009177D4` (길이 `84` bytes)
- VA: `0x0000000140917780`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0091779A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009177BF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PspJobDelete](../../text/4B/PspJobDelete_function_004BF8F0.md) at `0x004BFAD5`
- [NtCreateJobObject](NtCreateJobObject_function_009177E0.md) at `0x009179A6`

### Static image references
- `0x00917790` → RVA `0x00FD9DA8` (`PAGEDATA`; read)
- `0x0091779F` → RVA `0x00FD9DA8` (`PAGEDATA`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0091779A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009177BF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00917780  40 53                           push rbx
00917782  48 83 EC 20                     sub rsp, 0x20
00917786  66 FF 89 E6 01 00 00            dec word ptr [rcx + 0x1e6]
0091778D  45 33 C0                        xor r8d, r8d
00917790  48 8D 0D 11 26 6C 00            lea rcx, [rip + 0x6c2611]
00917797  33 D2                           xor edx, edx
00917799  90                              nop
0091779A  E8 91 8A 8F FF                  call 0x140210230
0091779F  F0 48 0F BA 2D FF 25 6C 00 00   lock bts qword ptr [rip + 0x6c25ff], 0
009177A9  48 8B D8                        mov rbx, rax
009177AC  73 16                           jae 0x1409177c4
009177AE  4C 8D 05 F3 25 6C 00            lea r8, [rip + 0x6c25f3]
009177B5  48 8B D0                        mov rdx, rax
009177B8  48 8D 0D E9 25 6C 00            lea rcx, [rip + 0x6c25e9]
009177BF  E8 CC 84 8F FF                  call 0x14020fc90
009177C4  48 85 DB                        test rbx, rbx
009177C7  74 04                           je 0x1409177cd
009177C9  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
009177CD  48 83 C4 20                     add rsp, 0x20
009177D1  5B                              pop rbx
009177D2  C3                              ret
009177D3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockJobListExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 7087633, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 7087603;
        a2 = result;
        a1 = v_rip + 7087593;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspLockJobListExclusive(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 7087633, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 7087603;
        Arg2 = result;
        Arg1 = v_rip + 7087593;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1E6` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00917780&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00917780[BB_00917780]
  bb_009177AE[BB_009177AE]
  bb_009177C4[BB_009177C4]
  bb_009177C9[BB_009177C9]
  bb_009177CD[BB_009177CD]
  bb_009177D3[BB_009177D3]
  bb_00917780 -->|branch| bb_009177C4
  bb_00917780 -->|fallthrough| bb_009177AE
  bb_009177AE -->|flow| bb_009177C4
  bb_009177C4 -->|branch| bb_009177CD
  bb_009177C4 -->|fallthrough| bb_009177C9
  bb_009177C9 -->|flow| bb_009177CD
```
