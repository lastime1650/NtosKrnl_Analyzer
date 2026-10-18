# sub_00B21240

- RVA: `0x00B21240`–`0x00B21253` (길이 `19` bytes)
- VA: `0x0000000140B21240`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00089120`
- 디코드: `4`개 명령, `19/19` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B21243` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B21243` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B2124E` → [ExpNtUpdateWnfStateData + 0x6EA](../90/ExpNtUpdateWnfStateData_function_0090A7A0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B21240  48 8B CB                        mov rcx, rbx
00B21243  E8 B8 03 7C FF                  call 0x1402e1600
00B21248  44 0F B6 64 24 54               movzx r12d, byte ptr [rsp + 0x54]
00B2124E  E9 37 9C DE FF                  jmp 0x14090ae8a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B21240(void)
{
    __int64 result;
    unsigned __int8 v_stack_p54;

    result = KeAbPostRelease(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B21240(void)
{
    int64_t result;
    uint8_t v_stack_p54;

    result = KeAbPostRelease(local_rbx, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B21240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B21240[BB_00B21240]
```
