# EtwpCopyJobGuidSafe

- RVA: `0x00A831CC`–`0x00A831E6` (길이 `26` bytes)
- VA: `0x0000000140A831CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [EtwTraceJobServerSiloMonitorCallback](../../text/64/EtwTraceJobServerSiloMonitorCallback_function_0064FB68.md) at `0x0064FBFA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A831CC  48 85 D2                        test rdx, rdx
00A831CF  74 0D                           je 0x140a831de
00A831D1  0F 10 82 C0 05 00 00            movups xmm0, xmmword ptr [rdx + 0x5c0]
00A831D8  F3 0F 7F 01                     movdqu xmmword ptr [rcx], xmm0
00A831DC  C3                              ret
00A831DD  CC                              int3
00A831DE  0F 57 C0                        xorps xmm0, xmm0
00A831E1  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A831E4  C3                              ret
00A831E5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall EtwpCopyJobGuidSafe(__int64 a1, __int64 a2)
{
    if (a2 == 0) goto loc_00A831DE;
    *(unsigned __int64 *)(a1) = v_xmm0;
    return;
loc_00A831DE:
    *(unsigned __int64 *)(a1) = v_xmm0;
    return;
}
```

## 5. (Beta) C Style

```c
void EtwpCopyJobGuidSafe(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (Arg2 == 0) goto loc_00A831DE;
    *(uint64_t *)(arg1) = v_xmm0;
    return;
loc_00A831DE:
    *(uint64_t *)(arg1) = v_xmm0;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x0` | `128` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A831CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A831CC[BB_00A831CC]
  bb_00A831D1[BB_00A831D1]
  bb_00A831DD[BB_00A831DD]
  bb_00A831DE[BB_00A831DE]
  bb_00A831E5[BB_00A831E5]
  bb_00A831CC -->|branch| bb_00A831DE
  bb_00A831CC -->|fallthrough| bb_00A831D1
  bb_00A831DD -->|flow| bb_00A831DE
```
