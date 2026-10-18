# HvlReadPerfMsr

- RVA: `0x00584CB0`–`0x00584CD7` (길이 `39` bytes)
- VA: `0x0000000140584CB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00584CCC` → [HvlpReadPerfRegister](HvlpReadPerfRegister_function_00585CBC.md) (function, `0x00585CBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00584CB0  48 83 EC 28                     sub rsp, 0x28
00584CB4  48 B8 00 00 00 00 00 00 10 00   movabs rax, 0x10000000000000
00584CBE  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00584CC3  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00584CC7  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00584CCC  E8 EB 0F 00 00                  call 0x140585cbc
00584CD1  48 83 C4 28                     add rsp, 0x28
00584CD5  C3                              ret
00584CD6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlReadPerfMsr(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (40);
    v_stack_p20 = result;
    v_stack_p20 = a2;
    result = HvlpReadPerfRegister(a1, v_stack_p20, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlReadPerfMsr(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (40);
    v_stack_p20 = result;
    v_stack_p20 = Arg2;
    result = HvlpReadPerfRegister(Arg1, v_stack_p20, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00584CB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00584CB0[BB_00584CB0]
  bb_00584CD6[BB_00584CD6]
```
