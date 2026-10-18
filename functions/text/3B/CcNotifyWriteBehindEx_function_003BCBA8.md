# CcNotifyWriteBehindEx

- RVA: `0x003BCBA8`–`0x003BCBC6` (길이 `30` bytes)
- VA: `0x00000001403BCBA8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `11`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003BCBBF` → [CcNotifyWriteBehindInternal](../3C/CcNotifyWriteBehindInternal_function_003CC224.md) (function, `0x003CC224`)

### Direct callers
- [MiObtainFreePages](MiObtainFreePages_function_003BB724.md) at `0x003BB774`
- [MiFlushAllPagesWorker](MiFlushAllPagesWorker_function_003BCED4.md) at `0x003BCF72`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003BCBA8  48 83 EC 28                     sub rsp, 0x28
003BCBAC  8B C1                           mov eax, ecx
003BCBAE  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
003BCBB2  48 85 C9                        test rcx, rcx
003BCBB5  75 06                           jne 0x1403bcbbd
003BCBB7  48 83 C4 28                     add rsp, 0x28
003BCBBB  C3                              ret
003BCBBC  CC                              int3
003BCBBD  8B D0                           mov edx, eax
003BCBBF  E8 60 F6 00 00                  call 0x1403cc224
003BCBC4  EB F1                           jmp 0x1403bcbb7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcNotifyWriteBehindEx(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a2 + 8) != 0) goto loc_003BCBBD;
loc_003BCBB7:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a1);
loc_003BCBBD:
    result = CcNotifyWriteBehindInternal(*(unsigned __int64 *)(a2 + 8), (unsigned int)((unsigned int)((unsigned int)(a1))), a3, a4);
    goto loc_003BCBB7;
}
```

## 5. (Beta) C Style

```c
int64_t CcNotifyWriteBehindEx(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg2 + 0x8) != 0) goto loc_003BCBBD;
loc_003BCBB7:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg1);
loc_003BCBBD:
    result = CcNotifyWriteBehindInternal(*(uint64_t *)(arg2 + 0x8), (uint32_t)((uint32_t)((uint32_t)(Arg1))), a3, a4);
    goto loc_003BCBB7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BCBA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003BCBA8[BB_003BCBA8]
  bb_003BCBB7[BB_003BCBB7]
  bb_003BCBBC[BB_003BCBBC]
  bb_003BCBBD[BB_003BCBBD]
  bb_003BCBA8 -->|branch| bb_003BCBBD
  bb_003BCBA8 -->|fallthrough| bb_003BCBB7
  bb_003BCBBC -->|flow| bb_003BCBBD
  bb_003BCBBD -->|branch| bb_003BCBB7
```
