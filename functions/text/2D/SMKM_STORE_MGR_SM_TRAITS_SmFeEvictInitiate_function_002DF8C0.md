# SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmFeEvictInitiate

- RVA: `0x002DF8C0`–`0x002DF8DD` (길이 `29` bytes)
- VA: `0x00000001402DF8C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070A48`
- 디코드: `6`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmpPageEvict](../24/SMKM_STORE_MGR_SM_TRAITS_SmpPageEvict_function_0024A5F4.md) at `0x0024A634`

### Static image references
- `0x002DF8CB` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DF8C0  4C 8B DC                        mov r11, rsp
002DF8C3  53                              push rbx
002DF8C4  48 81 EC 30 01 00 00            sub rsp, 0x130
002DF8CB  48 8B 05 6E AE B2 00            mov rax, qword ptr [rip + 0xb2ae6e]
002DF8D2  48 33 C4                        xor rax, rsp
002DF8D5  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_MGR_SM_TRAITS___SmFeEvictInitiate(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 11710062)) ^ (v_rsp);
    v_stack_m58 = result;
    return result;
}
```

## 5. (Beta) C Style

```c
void SMKM_STORE_MGR_SM_TRAITS___SmFeEvictInitiate(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0xB2AE6E)) ^ (local_rsp);
    v_stack_m58 = result;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DF8C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002DF8C0[BB_002DF8C0]
```
