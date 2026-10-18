# ExpInitializeThreadHistory

- RVA: `0x00497CD0`–`0x00497CE4` (길이 `20` bytes)
- VA: `0x0000000140497CD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtCreateWorkerFactory](../../page/9A/NtCreateWorkerFactory_function_009A7E10.md) at `0x009A80D5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00497CD0  83 A1 98 01 00 00 F8            and dword ptr [rcx + 0x198], 0xfffffff8
00497CD7  0F 57 C0                        xorps xmm0, xmm0
00497CDA  0F 11 41 48                     movups xmmword ptr [rcx + 0x48], xmm0
00497CDE  0F 11 41 58                     movups xmmword ptr [rcx + 0x58], xmm0
00497CE2  C3                              ret
00497CE3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall ExpInitializeThreadHistory(__int64 a1)
{
    *(unsigned __int64 *)(a1 + 72) = v_xmm0;
    *(unsigned __int64 *)(a1 + 88) = v_xmm0;
    return;
}
```

## 5. (Beta) C Style

```c
void ExpInitializeThreadHistory(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(arg1 + 0x48) = v_xmm0;
    *(uint64_t *)(arg1 + 0x58) = v_xmm0;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `128` | `R` |
| `Arg1` | `+ 0x58` | `128` | `R` |
| `Arg1` | `+ 0x198` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00497CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00497CD0[BB_00497CD0]
  bb_00497CE3[BB_00497CE3]
```
