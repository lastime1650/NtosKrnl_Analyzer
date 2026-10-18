# HvMoveLayoutStats

- RVA: `0x0096DAD0`–`0x0096DAE3` (길이 `19` bytes)
- VA: `0x000000014096DAD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvCheckHive](HvCheckHive_function_0096D550.md) at `0x0096D672`
- [HvCheckBin](HvCheckBin_function_0096D790.md) at `0x0096D8A8`
- [HvCheckBin](HvCheckBin_function_0096D790.md) at `0x0096D8B1`
- [HvCheckBin](HvCheckBin_function_0096D790.md) at `0x0096D8EE`
- [HvCheckBin](HvCheckBin_function_0096D790.md) at `0x0096D9AD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0096DAD0  8B 41 08                        mov eax, dword ptr [rcx + 8]
0096DAD3  01 01                           add dword ptr [rcx], eax
0096DAD5  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
0096DAD8  01 41 04                        add dword ptr [rcx + 4], eax
0096DADB  33 C0                           xor eax, eax
0096DADD  48 89 41 08                     mov qword ptr [rcx + 8], rax
0096DAE1  C3                              ret
0096DAE2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvMoveLayoutStats(__int64 a1)
{
    __int64 result;

    result = 0;
    *(unsigned __int64 *)(a1 + 8) = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvMoveLayoutStats(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    *(uint64_t *)(arg1 + 0x8) = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x4` | `32` | `R/W` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0xC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096DAD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0096DAD0[BB_0096DAD0]
  bb_0096DAE2[BB_0096DAE2]
```
