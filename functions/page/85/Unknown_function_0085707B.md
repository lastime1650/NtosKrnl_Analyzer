# sub_0085707B

- RVA: `0x0085707B`–`0x00857093` (길이 `24` bytes)
- VA: `0x000000014085707B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A5DC`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00857089` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00857089` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0085707E` → [CmpGetValueData + 0xBE](CmpGetValueData_function_00856DB0.md) (`tail-transfer`)
  - `0x0085708E` → [CmpGetValueData + 0xBE](CmpGetValueData_function_00856DB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085707B  48 85 FF                        test rdi, rdi
0085707E  0F 84 EA FD FF FF               je 0x140856e6e
00857084  33 D2                           xor edx, edx
00857086  48 8B CF                        mov rcx, rdi
00857089  E8 E2 B7 32 00                  call 0x140b82870
0085708E  E9 DB FD FF FF                  jmp 0x140856e6e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085707B(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    result = ExFreePoolWithTag(v_rdi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0085707B(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    result = ExFreePoolWithTag(local_rdi, Arg2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085707B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085707B[BB_0085707B]
  bb_00857084[BB_00857084]
  bb_0085707B -->|fallthrough| bb_00857084
```
