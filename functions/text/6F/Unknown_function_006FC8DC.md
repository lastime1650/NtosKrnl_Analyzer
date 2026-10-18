# sub_006FC8DC

- RVA: `0x006FC8DC`–`0x006FC8F3` (길이 `23` bytes)
- VA: `0x00000001406FC8DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBFE0`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006FC8E6` → [AuthzBasepCompareOctetStringOperands + 0x69](../4B/AuthzBasepCompareOctetStringOperands_function_004BD4A8.md) (`tail-transfer`)
  - `0x006FC8EE` → [AuthzBasepCompareOctetStringOperands + 0x8C](../4B/AuthzBasepCompareOctetStringOperands_function_004BD4A8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FC8DC  83 C8 FF                        or eax, 0xffffffff
006FC8DF  3B 7C 24 38                     cmp edi, dword ptr [rsp + 0x38]
006FC8E3  0F 42 C8                        cmovb ecx, eax
006FC8E6  E9 26 0C DC FF                  jmp 0x1404bd511
006FC8EB  41 8B C8                        mov ecx, r8d
006FC8EE  E9 41 0C DC FF                  jmp 0x1404bd534
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FC8DC(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7)
{
    __int64 result;

    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(v_rdi)) < a7) { a1 = (unsigned int)(result); }
}
```

## 5. (Beta) C Style

```c
int64_t sub_006FC8DC(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint32_t Arg7)
{
    int64_t result;

    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(local_rdi)) < Arg7) { Arg1 = (uint32_t)(result); }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FC8DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FC8DC[BB_006FC8DC]
  bb_006FC8EB[BB_006FC8EB]
```
