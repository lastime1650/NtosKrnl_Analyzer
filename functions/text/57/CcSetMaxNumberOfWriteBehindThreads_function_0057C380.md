# CcSetMaxNumberOfWriteBehindThreads

- RVA: `0x0057C380`–`0x0057C39A` (길이 `26` bytes)
- VA: `0x000000014057C380`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CcAdjustWriteBehindThreadPool](CcAdjustWriteBehindThreadPool_function_0057B684.md) at `0x0057B6B3`
- [CcAdjustWriteBehindThreadPool](CcAdjustWriteBehindThreadPool_function_0057B684.md) at `0x0057B6CD`

### Static image references
- `0x0057C380` → RVA `0x00E0A874` (`.data`; read)
- `0x0057C389` → RVA `0x00E65B88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057C380  83 3D ED E4 88 00 01            cmp dword ptr [rip + 0x88e4ed], 1
0057C387  77 0F                           ja 0x14057c398
0057C389  80 3D F8 97 8E 00 00            cmp byte ptr [rip + 0x8e97f8], 0
0057C390  75 06                           jne 0x14057c398
0057C392  89 91 08 05 00 00               mov dword ptr [rcx + 0x508], edx
0057C398  C3                              ret
0057C399  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall CcSetMaxNumberOfWriteBehindThreads(__int64 a1, int a2)
{
    if ((*(unsigned int *)(v_rip + 8971501)) > 1) goto loc_0057C398;
    if ((*(unsigned __int8 *)(v_rip + 9345016)) == 0) {
        *(unsigned int *)(a1 + 1288) = a2;
    }
    return;
}
```

## 5. (Beta) C Style

```c
void CcSetMaxNumberOfWriteBehindThreads(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((*(uint32_t *)(v_rip + 0x88E4ED)) > 1) goto loc_0057C398;
    if ((*(uint8_t *)(v_rip + 0x8E97F8)) == 0) {
        *(uint32_t *)(arg1 + 0x508) = Arg2;
    }
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x508` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057C380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057C380[BB_0057C380]
  bb_0057C389[BB_0057C389]
  bb_0057C392[BB_0057C392]
  bb_0057C398[BB_0057C398]
  bb_0057C399[BB_0057C399]
  bb_0057C380 -->|branch| bb_0057C398
  bb_0057C380 -->|fallthrough| bb_0057C389
  bb_0057C389 -->|branch| bb_0057C398
  bb_0057C389 -->|fallthrough| bb_0057C392
  bb_0057C392 -->|flow| bb_0057C398
```
