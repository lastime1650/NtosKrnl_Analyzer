# KeInitializeWaitChain

- RVA: `0x00438EB0`–`0x00438EB7` (길이 `7` bytes)
- VA: `0x0000000140438EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `7/7` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VrpAllocateDiffHiveEntry](../../page/85/VrpAllocateDiffHiveEntry_function_0085E320.md) at `0x0085E3BE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00438EB0  33 C0                           xor eax, eax
00438EB2  48 89 01                        mov qword ptr [rcx], rax
00438EB5  C3                              ret
00438EB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInitializeWaitChain(__int64 a1)
{
    __int64 result;

    result = 0;
    *(unsigned __int64 *)(a1) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeInitializeWaitChain(void *WaitChain)
{
    uint8_t *waitChain = (uint8_t *)WaitChain;

    int64_t result;

    result = 0;
    *(uint64_t *)(waitChain) = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `WaitChain` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00438EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00438EB0[BB_00438EB0]
  bb_00438EB6[BB_00438EB6]
```
