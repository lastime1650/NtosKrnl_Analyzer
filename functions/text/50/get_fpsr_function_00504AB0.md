# get_fpsr

- RVA: `0x00504AB0`–`0x00504AC0` (길이 `16` bytes)
- VA: `0x0000000140504AB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C28B8`
- 디코드: `5`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [clrfp](clrfp_function_00504980.md) at `0x00504986`
- [ctrlfp](ctrlfp_function_005049B0.md) at `0x005049C5`
- [set_statfp](set_statfp_function_00504A40.md) at `0x00504A49`
- [statfp](statfp_function_00504A70.md) at `0x00504A74`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00504AB0  48 83 EC 08                     sub rsp, 8
00504AB4  0F AE 1C 24                     stmxcsr dword ptr [rsp]
00504AB8  8B 04 24                        mov eax, dword ptr [rsp]
00504ABB  48 83 C4 08                     add rsp, 8
00504ABF  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall get_fpsr(void)
{
    __int64 v_rsp;
    unsigned int v_stack_m8;

    v_rsp = (v_rsp) - (8);
    v_rsp = (v_rsp) + (8);
    return (unsigned int)(v_stack_m8);
}
```

## 5. (Beta) C Style

```c
void get_fpsr(void)
{
    int64_t local_rsp;
    uint32_t v_stack_m8;

    local_rsp = (local_rsp) - (8);
    local_rsp = (local_rsp) + (8);
    return (uint32_t)(v_stack_m8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00504AB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00504AB0[BB_00504AB0]
```
