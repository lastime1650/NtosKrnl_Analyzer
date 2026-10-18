# MiZeroPageWorkMapping

- RVA: `0x00436CE0`–`0x00436D00` (길이 `32` bytes)
- VA: `0x0000000140436CE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A30D0`
- 디코드: `8`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiPageListCollision](MiPageListCollision_function_00436B48.md) at `0x00436BAB`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x00694793`
- [MiScrubLargePage](../69/MiScrubLargePage_function_006942E8.md) at `0x00694806`

### Static image references
- `0x00436CEE` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00436CE0  4C 8B DC                        mov r11, rsp
00436CE3  53                              push rbx
00436CE4  55                              push rbp
00436CE5  41 55                           push r13
00436CE7  48 81 EC 40 01 00 00            sub rsp, 0x140
00436CEE  48 8B 05 4B 3A 9D 00            mov rax, qword ptr [rip + 0x9d3a4b]
00436CF5  48 33 C4                        xor rax, rsp
00436CF8  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiZeroPageWorkMapping(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (320);
    result = (*(unsigned __int64 *)(v_rip + 10304075)) ^ (v_rsp);
    v_stack_m48 = result;
    return result;
}
```

## 5. (Beta) C Style

```c
void MiZeroPageWorkMapping(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (320);
    result = (*(uint64_t *)(v_rip + 0x9D3A4B)) ^ (local_rsp);
    v_stack_m48 = result;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00436CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00436CE0[BB_00436CE0]
```
