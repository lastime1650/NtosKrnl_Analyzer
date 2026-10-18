# sub_008E46F9

- RVA: `0x008E46F9`–`0x008E4711` (길이 `24` bytes)
- VA: `0x00000001408E46F9`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086414`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008E4703` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008E4703` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008E46FC` → [sub_008E4675 + 0x58](Unknown_function_008E4675.md) (`tail-transfer`)
  - `0x008E470F` → [sub_008E4675 + 0x58](Unknown_function_008E4675.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E46F9  45 85 E4                        test r12d, r12d
008E46FC  74 CF                           je 0x1408e46cd
008E46FE  48 8B 0F                        mov rcx, qword ptr [rdi]
008E4701  33 D2                           xor edx, edx
008E4703  E8 68 E1 29 00                  call 0x140b82870
008E4708  48 C7 07 00 00 00 00            mov qword ptr [rdi], 0
008E470F  EB BC                           jmp 0x1408e46cd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008E46F9(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rdi), a2, a3, a4);
    *(unsigned __int64 *)(v_rdi) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008E46F9(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rdi), Arg2, a3, a4);
    *(uint64_t *)(local_rdi) = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E46F9&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E46F9[BB_008E46F9]
  bb_008E46FE[BB_008E46FE]
  bb_008E46F9 -->|fallthrough| bb_008E46FE
```
