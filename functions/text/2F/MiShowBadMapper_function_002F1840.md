# MiShowBadMapper

- RVA: `0x002F1840`–`0x002F1861` (길이 `33` bytes)
- VA: `0x00000001402F1840`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071E20`
- 디코드: `8`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInsertPhysicalPteMapping](../2A/MiInsertPhysicalPteMapping_function_002AE26C.md) at `0x002AE445`
- [MiFillSystemPtes](../31/MiFillSystemPtes_function_00319850.md) at `0x0031A2C4`
- [MiDecommitFreePagesTail](../41/MiDecommitFreePagesTail_function_0041ECE0.md) at `0x0041F09D`
- [MiMapMdlCommon](../67/MiMapMdlCommon_function_00674524.md) at `0x00674674`

### Static image references
- `0x002F184F` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F1840  4C 8B DC                        mov r11, rsp
002F1843  53                              push rbx
002F1844  41 56                           push r14
002F1846  41 57                           push r15
002F1848  48 81 EC 20 01 00 00            sub rsp, 0x120
002F184F  48 8B 05 EA 8E B1 00            mov rax, qword ptr [rip + 0xb18eea]
002F1856  48 33 C4                        xor rax, rsp
002F1859  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiShowBadMapper(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (288);
    result = (*(unsigned __int64 *)(v_rip + 11636458)) ^ (v_rsp);
    v_stack_m48 = result;
    return result;
}
```

## 5. (Beta) C Style

```c
void MiShowBadMapper(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (288);
    result = (*(uint64_t *)(v_rip + 0xB18EEA)) ^ (local_rsp);
    v_stack_m48 = result;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F1840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F1840[BB_002F1840]
```
