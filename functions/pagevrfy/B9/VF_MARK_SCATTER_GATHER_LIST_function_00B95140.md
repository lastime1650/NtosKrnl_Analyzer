# VF_MARK_SCATTER_GATHER_LIST

- RVA: `0x00B95140`–`0x00B95157` (길이 `23` bytes)
- VA: `0x0000000140B95140`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VfBuildMdlFromScatterGatherList](VfBuildMdlFromScatterGatherList_function_00B95940.md) at `0x00B959F6`
- [ViScatterGatherCallback](ViScatterGatherCallback_function_00B99B20.md) at `0x00B99B72`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B95140  48 85 D2                        test rdx, rdx
00B95143  74 10                           je 0x140b95155
00B95145  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
00B95149  48 89 42 30                     mov qword ptr [rdx + 0x30], rax
00B9514D  48 C7 41 08 0D F0 AD DE         mov qword ptr [rcx + 8], 0xffffffffdeadf00d
00B95155  C3                              ret
00B95156  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VF_MARK_SCATTER_GATHER_LIST(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a2 != 0) {
        result = *(unsigned __int64 *)(a1 + 8);
        *(unsigned __int64 *)(a2 + 48) = result;
        *(unsigned __int64 *)(a1 + 8) = 0xFFFFFFFFDEADF00DULL;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VF_MARK_SCATTER_GATHER_LIST(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 != 0) {
        result = *(uint64_t *)(arg1 + 0x8);
        *(uint64_t *)(Arg2 + 0x30) = result;
        *(uint64_t *)(arg1 + 0x8) = 0xFFFFFFFFDEADF00DULL;
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B95140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B95140[BB_00B95140]
  bb_00B95145[BB_00B95145]
  bb_00B95155[BB_00B95155]
  bb_00B95156[BB_00B95156]
  bb_00B95140 -->|branch| bb_00B95155
  bb_00B95140 -->|fallthrough| bb_00B95145
  bb_00B95145 -->|flow| bb_00B95155
```
