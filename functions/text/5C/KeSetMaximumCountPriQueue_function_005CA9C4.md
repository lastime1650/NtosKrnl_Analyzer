# KeSetMaximumCountPriQueue

- RVA: `0x005CA9C4`–`0x005CA9D6` (길이 `18` bytes)
- VA: `0x00000001405CA9C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpWorkQueueManagerThread](../../page/AF/ExpWorkQueueManagerThread_function_00AF6D60.md) at `0x00AF7286`

### Static image references
- `0x005CA9C8` → RVA `0x00FC6A80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CA9C4  85 D2                           test edx, edx
005CA9C6  75 06                           jne 0x1405ca9ce
005CA9C8  8B 15 B2 C0 9F 00               mov edx, dword ptr [rip + 0x9fc0b2]
005CA9CE  89 91 98 02 00 00               mov dword ptr [rcx + 0x298], edx
005CA9D4  C3                              ret
005CA9D5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KeSetMaximumCountPriQueue(__int64 a1, int a2)
{
    if (a2 == 0) {
        a2 = *(unsigned int *)(v_rip + 10469554);
    }
    *(unsigned int *)(a1 + 664) = a2;
    return;
}
```

## 5. (Beta) C Style

```c
void KeSetMaximumCountPriQueue(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg2 == 0) {
        Arg2 = *(uint32_t *)(v_rip + 0x9FC0B2);
    }
    *(uint32_t *)(arg1 + 0x298) = Arg2;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x298` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CA9C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CA9C4[BB_005CA9C4]
  bb_005CA9C8[BB_005CA9C8]
  bb_005CA9CE[BB_005CA9CE]
  bb_005CA9D5[BB_005CA9D5]
  bb_005CA9C4 -->|branch| bb_005CA9CE
  bb_005CA9C4 -->|fallthrough| bb_005CA9C8
  bb_005CA9C8 -->|flow| bb_005CA9CE
```
