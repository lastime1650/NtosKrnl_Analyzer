# HalpResumePoint

- RVA: `0x006ACDE0`–`0x006ACDFD` (길이 `29` bytes)
- VA: `0x00000001406ACDE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFDBC`
- 디코드: `7`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006ACDEE` → [KasanHibernationResume](../5A/KasanHibernationResume_function_005AACE0.md) (function, `0x005AACE0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006ACDE0  48 83 EC 30                     sub rsp, 0x30
006ACDE4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
006ACDE9  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
006ACDEE  E8 ED DE EF FF                  call 0x1405aace0
006ACDF3  48 83 C4 28                     add rsp, 0x28
006ACDF7  B8 01 00 00 00                  mov eax, 1
006ACDFC  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpResumePoint(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_p0;

    v_rsp = (v_rsp) - (48);
    v_stack_m8 = result;
    result = KasanHibernationResume(a1, v_stack_p0, a3, a4);
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
void HalpResumePoint(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_p0;

    local_rsp = (local_rsp) - (48);
    v_stack_m8 = result;
    result = KasanHibernationResume(a1, v_stack_p0, a3, a4);
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006ACDE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006ACDE0[BB_006ACDE0]
```
