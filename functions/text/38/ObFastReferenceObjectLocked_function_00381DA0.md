# ObFastReferenceObjectLocked

- RVA: `0x00381DA0`–`0x00381DC1` (길이 `33` bytes)
- VA: `0x0000000140381DA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00381DB2` → [ObfReferenceObjectWithTag](../21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)

### Direct callers
- [MiCompleteProtoPteFault](../34/MiCompleteProtoPteFault_function_00345710.md) at `0x003464FB`
- [MiPrepareToFlushSubsection](../36/MiPrepareToFlushSubsection_function_00369094.md) at `0x003690D4`
- [sub_00380A2B](Unknown_function_00380A2B.md) at `0x00380A49`
- [IopQueueIrpToFileObject](../40/IopQueueIrpToFileObject_function_00409864.md) at `0x004099A4`
- [MiNotifyUserOfLostData](../67/MiNotifyUserOfLostData_function_00678280.md) at `0x0067830A`
- [MiNoPagesLastChance](../68/MiNoPagesLastChance_function_0068B22C.md) at `0x0068B619`
- [ObpLookupObjectName](../../page/89/ObpLookupObjectName_function_0089BE90.md) at `0x0089D694`
- [sub_00B1BBD6](../../page/B1/Unknown_function_00B1BBD6.md) at `0x00B1BBE7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00381DA0  40 53                           push rbx
00381DA2  48 83 EC 20                     sub rsp, 0x20
00381DA6  48 8B 19                        mov rbx, qword ptr [rcx]
00381DA9  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
00381DAD  74 08                           je 0x140381db7
00381DAF  48 8B CB                        mov rcx, rbx
00381DB2  E8 59 E9 E8 FF                  call 0x140210710
00381DB7  48 8B C3                        mov rax, rbx
00381DBA  48 83 C4 20                     add rsp, 0x20
00381DBE  5B                              pop rbx
00381DBF  C3                              ret
00381DC0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObFastReferenceObjectLocked(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    v_rbx = (*(unsigned __int64 *)(a1)) & (-16);
    if (!(condition_is_equal)) {
        a1 = v_rbx;
        result = ObfReferenceObjectWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t ObFastReferenceObjectLocked(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    local_rbx = (*(uint64_t *)(arg1)) & (-16);
    if (!(condition_is_equal)) {
        Arg1 = local_rbx;
        result = ObfReferenceObjectWithTag(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00381DA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00381DA0[BB_00381DA0]
  bb_00381DAF[BB_00381DAF]
  bb_00381DB7[BB_00381DB7]
  bb_00381DC0[BB_00381DC0]
  bb_00381DA0 -->|branch| bb_00381DB7
  bb_00381DA0 -->|fallthrough| bb_00381DAF
  bb_00381DAF -->|flow| bb_00381DB7
```
