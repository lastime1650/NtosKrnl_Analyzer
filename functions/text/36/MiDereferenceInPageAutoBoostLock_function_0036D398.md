# MiDereferenceInPageAutoBoostLock

- RVA: `0x0036D398`–`0x0036D3C6` (길이 `46` bytes)
- VA: `0x000000014036D398`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `15`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0036D3B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [sub_0036C6B5](Unknown_function_0036C6B5.md) at `0x0036CA12`
- [sub_0036CB1C](Unknown_function_0036CB1C.md) at `0x0036CB98`
- [sub_0036CFD7](Unknown_function_0036CFD7.md) at `0x0036D07B`
- [MmPrefetchPagesEx](../../page/93/MmPrefetchPagesEx_function_0093C9A0.md) at `0x0093CB1C`
- [MiPrefetchControlArea](../../page/93/MiPrefetchControlArea_function_0093E830.md) at `0x0093E8F1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0036D3B2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0036D398  48 83 EC 28                     sub rsp, 0x28
0036D39C  48 83 C8 FF                     or rax, 0xffffffffffffffff
0036D3A0  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0036D3A5  48 83 E8 01                     sub rax, 1
0036D3A9  7F 0C                           jg 0x14036d3b7
0036D3AB  48 85 C0                        test rax, rax
0036D3AE  75 0D                           jne 0x14036d3bd
0036D3B0  33 D2                           xor edx, edx
0036D3B2  E8 B9 54 81 00                  call 0x140b82870
0036D3B7  48 83 C4 28                     add rsp, 0x28
0036D3BB  C3                              ret
0036D3BC  CC                              int3
0036D3BD  B9 0E 00 00 00                  mov ecx, 0xe
0036D3C2  CD 29                           int 0x29
0036D3C4  EB F1                           jmp 0x14036d3b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDereferenceInPageAutoBoostLock(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_0036D3B7;
    if (result != 0) goto loc_0036D3BD;
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
loc_0036D3B7:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0036D3BD:
    goto loc_0036D3B7;
}
```

## 5. (Beta) C Style

```c
int64_t MiDereferenceInPageAutoBoostLock(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (result) | (-1);
    result = (result) - (1);
    if (condition_is_greater) goto loc_0036D3B7;
    if (result != 0) goto loc_0036D3BD;
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
loc_0036D3B7:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0036D3BD:
    goto loc_0036D3B7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0036D398&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0036D398[BB_0036D398]
  bb_0036D3AB[BB_0036D3AB]
  bb_0036D3B0[BB_0036D3B0]
  bb_0036D3B7[BB_0036D3B7]
  bb_0036D3BC[BB_0036D3BC]
  bb_0036D3BD[BB_0036D3BD]
  bb_0036D398 -->|branch| bb_0036D3B7
  bb_0036D398 -->|fallthrough| bb_0036D3AB
  bb_0036D3AB -->|branch| bb_0036D3BD
  bb_0036D3AB -->|fallthrough| bb_0036D3B0
  bb_0036D3B0 -->|flow| bb_0036D3B7
  bb_0036D3BC -->|flow| bb_0036D3BD
  bb_0036D3BD -->|branch| bb_0036D3B7
```
