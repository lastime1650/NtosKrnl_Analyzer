# MiFillCommitReturnInfo

- RVA: `0x00447990`–`0x004479A1` (길이 `17` bytes)
- VA: `0x0000000140447990`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiDecommitRegion](../../page/88/MiDecommitRegion_function_008807A0.md) at `0x008808AB`
- [MiRemoveVadCharges](../../page/9B/MiRemoveVadCharges_function_009BAEC4.md) at `0x009BAF69`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00447990  48 2B 4A 10                     sub rcx, qword ptr [rdx + 0x10]
00447994  49 89 08                        mov qword ptr [r8], rcx
00447997  48 2B 4A 08                     sub rcx, qword ptr [rdx + 8]
0044799B  49 89 48 08                     mov qword ptr [r8 + 8], rcx
0044799F  C3                              ret
004479A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiFillCommitReturnInfo(__int64 a1, __int64 a2, __int64 a3)
{
    a1 = (a1) - (*(unsigned __int64 *)(a2 + 16));
    *(unsigned __int64 *)(a3) = a1;
    a1 = (a1) - (*(unsigned __int64 *)(a2 + 8));
    *(unsigned __int64 *)(a3 + 8) = a1;
    return;
}
```

## 5. (Beta) C Style

```c
void MiFillCommitReturnInfo(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    Arg1 = (Arg1) - (*(uint64_t *)(arg2 + 0x10));
    *(uint64_t *)(arg3) = Arg1;
    Arg1 = (Arg1) - (*(uint64_t *)(arg2 + 0x8));
    *(uint64_t *)(arg3 + 0x8) = Arg1;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00447990&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00447990[BB_00447990]
  bb_004479A0[BB_004479A0]
```
