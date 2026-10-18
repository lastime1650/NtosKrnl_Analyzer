# HvpEnlistFreeCells

- RVA: `0x0085AC00`–`0x0085AC29` (길이 `41` bytes)
- VA: `0x000000014085AC00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AD28`
- 디코드: `13`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvpBuildMapForMemoryBackedHive](../7F/HvpBuildMapForMemoryBackedHive_function_007F3B4C.md) at `0x007F3CB2`
- [HvpRemapAndEnlistHiveBins](../9B/HvpRemapAndEnlistHiveBins_function_009B8E0C.md) at `0x009B93A9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0085AC00  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0085AC05  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0085AC0A  53                              push rbx
0085AC0B  55                              push rbp
0085AC0C  41 54                           push r12
0085AC0E  41 55                           push r13
0085AC10  41 56                           push r14
0085AC12  41 57                           push r15
0085AC14  48 83 EC 58                     sub rsp, 0x58
0085AC18  4C 8B 69 38                     mov r13, qword ptr [rcx + 0x38]
0085AC1C  45 8B E0                        mov r12d, r8d
0085AC1F  83 81 90 00 00 00 20            add dword ptr [rcx + 0x90], 0x20
0085AC26  48 8B EA                        mov rbp, rdx
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall HvpEnlistFreeCells(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 v_rsp;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (88);
    return;
}
```

## 5. (Beta) C Style

```c
void HvpEnlistFreeCells(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (88);
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085AC00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085AC00[BB_0085AC00]
```
