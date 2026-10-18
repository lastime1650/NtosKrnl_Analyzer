# EtwpUpdateEventsLostCount

- RVA: `0x003F18E0`–`0x003F18FD` (길이 `29` bytes)
- VA: `0x00000001403F18E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) at `0x0025D378`
- [EtwpLogSystemEventUnsafe](../2F/EtwpLogSystemEventUnsafe_function_002FBF10.md) at `0x002FC624`
- [EtwpReserveTraceBuffer](../2F/EtwpReserveTraceBuffer_function_002FC8C0.md) at `0x002FCE5A`
- [EtwpFailLogging](EtwpFailLogging_function_003F0A50.md) at `0x003F0B57`
- [EtwpFailLogging](EtwpFailLogging_function_003F0A50.md) at `0x003F0C4D`
- [EtwpCompressBuffer](../65/EtwpCompressBuffer_function_00652DBC.md) at `0x00652F83`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003F18E0  F0 FF 81 F0 00 00 00            lock inc dword ptr [rcx + 0xf0]
003F18E7  8B 81 30 03 00 00               mov eax, dword ptr [rcx + 0x330]
003F18ED  A8 08                           test al, 8
003F18EF  74 0A                           je 0x1403f18fb
003F18F1  C7 81 C0 01 00 00 01 00 00 00   mov dword ptr [rcx + 0x1c0], 1
003F18FB  C3                              ret
003F18FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpUpdateEventsLostCount(__int64 a1)
{
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 816)))) & (8)) != 0) {
        *(unsigned int *)(a1 + 448) = 1;
    }
    return (unsigned int)(*(unsigned int *)(a1 + 816));
}
```

## 5. (Beta) C Style

```c
int64_t EtwpUpdateEventsLostCount(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x330)))) & (8)) != 0) {
        *(uint32_t *)(arg1 + 0x1C0) = 1;
    }
    return (uint32_t)(*(uint32_t *)(arg1 + 0x330));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `32` | `R/W` |
| `Arg1` | `+ 0x1C0` | `32` | `W` |
| `Arg1` | `+ 0x330` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F18E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F18E0[BB_003F18E0]
  bb_003F18F1[BB_003F18F1]
  bb_003F18FB[BB_003F18FB]
  bb_003F18FC[BB_003F18FC]
  bb_003F18E0 -->|branch| bb_003F18FB
  bb_003F18E0 -->|fallthrough| bb_003F18F1
  bb_003F18F1 -->|flow| bb_003F18FB
```
