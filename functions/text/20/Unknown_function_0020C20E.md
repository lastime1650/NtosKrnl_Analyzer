# sub_0020C20E

- RVA: `0x0020C20E`–`0x0020C222` (길이 `20` bytes)
- VA: `0x000000014020C20E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D89C`
- 디코드: `5`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0020C215` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0020C21D` → [KeRemoveQueueEx + 0x6A](KeRemoveQueueEx_function_0020BD30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0020C20E  0F B6 D1                        movzx edx, cl
0020C211  40 0F B6 CE                     movzx ecx, sil
0020C215  E8 E2 94 2E 00                  call 0x1404f56fc
0020C21A  45 33 C9                        xor r9d, r9d
0020C21D  E9 78 FB FF FF                  jmp 0x14020bd9a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0020C20E(unsigned __int8 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_rsi), a1, a3, a4);
    a4 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0020C20E(uint8_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;

    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_rsi), Arg1, Arg3, Arg4);
    Arg4 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0020C20E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0020C20E[BB_0020C20E]
```
