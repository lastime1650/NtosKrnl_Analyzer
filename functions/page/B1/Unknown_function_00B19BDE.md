# sub_00B19BDE

- RVA: `0x00B19BDE`–`0x00B19BFD` (길이 `31` bytes)
- VA: `0x0000000140B19BDE`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007EC9C`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B19BEA` → [FsRtlFreeExtraCreateParameterList](../8A/FsRtlFreeExtraCreateParameterList_function_008A1420.md) (function, `0x008A1420`)
- `0x00B19BF2` → [IoClearIrpExtraCreateParameter](../../text/59/IoClearIrpExtraCreateParameter_function_005979B0.md) (function, `0x005979B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B19BF2` → [IoClearIrpExtraCreateParameter](../../text/59/IoClearIrpExtraCreateParameter_function_005979B0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B19BE1` → [IopSymlinkAllocateAndAddECP + 0x7C](../8A/IopSymlinkAllocateAndAddECP_function_008A1E20.md) (`tail-transfer`)
  - `0x00B19BF8` → [IopSymlinkAllocateAndAddECP + 0x7C](../8A/IopSymlinkAllocateAndAddECP_function_008A1E20.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B19BDE  45 84 F6                        test r14b, r14b
00B19BE1  0F 84 B5 82 D8 FF               je 0x1408a1e9c
00B19BE7  48 8B CB                        mov rcx, rbx
00B19BEA  E8 31 78 D8 FF                  call 0x1408a1420
00B19BEF  48 8B CD                        mov rcx, rbp
00B19BF2  E8 B9 DD A7 FF                  call 0x1405979b0
00B19BF7  90                              nop
00B19BF8  E9 9F 82 D8 FF                  jmp 0x1408a1e9c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B19BDE(void)
{
    __int64 result;

    result = FsRtlFreeExtraCreateParameterList(v_rbx, a2, a3, a4);
    result = IoClearIrpExtraCreateParameter(v_rbp, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B19BDE(void)
{
    int64_t result;

    result = FsRtlFreeExtraCreateParameterList(local_rbx, a2, a3, a4);
    result = IoClearIrpExtraCreateParameter(local_rbp, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B19BDE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B19BDE[BB_00B19BDE]
  bb_00B19BE7[BB_00B19BE7]
  bb_00B19BDE -->|fallthrough| bb_00B19BE7
```
