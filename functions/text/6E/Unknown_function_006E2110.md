# sub_006E2110

- RVA: `0x006E2110`–`0x006E2127` (길이 `23` bytes)
- VA: `0x00000001406E2110`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078240`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E2115` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006E2115` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E2122` → [MiEmptyPageAccessLog + 0x2D5](../34/MiEmptyPageAccessLog_function_00348700.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E2110  48 8B 1B                        mov rbx, qword ptr [rbx]
006E2113  33 D2                           xor edx, edx
006E2115  E8 56 07 4A 00                  call 0x140b82870
006E211A  48 8B CB                        mov rcx, rbx
006E211D  48 85 DB                        test rbx, rbx
006E2120  75 EE                           jne 0x1406e2110
006E2122  E9 AE 68 C6 FF                  jmp 0x1403489d5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E2110(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_006E2110;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E2110(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    if (*(uint64_t *)(local_rbx) != 0) goto loc_006E2110;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E2110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E2110[BB_006E2110]
  bb_006E2122[BB_006E2122]
  bb_006E2110 -->|branch| bb_006E2110
  bb_006E2110 -->|fallthrough| bb_006E2122
```
