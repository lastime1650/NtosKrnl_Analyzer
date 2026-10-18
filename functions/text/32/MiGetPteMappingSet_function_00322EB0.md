# MiGetPteMappingSet

- RVA: `0x00322EB0`–`0x00322EC8` (길이 `24` bytes)
- VA: `0x0000000140322EB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075888`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_002B1BCF](../2B/Unknown_function_002B1BCF.md) at `0x002B1C99`
- [MiSlowRotateCopy](../67/MiSlowRotateCopy_function_0067E2B0.md) at `0x0067E355`
- [MiCopyFilePage](../68/MiCopyFilePage_function_00680790.md) at `0x006807C0`
- [MiFillPageWithImageExtentContents](../68/MiFillPageWithImageExtentContents_function_00680E44.md) at `0x00680EB4`
- [MiCopyMemoryPagefileData](../69/MiCopyMemoryPagefileData_function_00694C04.md) at `0x00694DE8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00322EC2` → [sub_00322F5E](Unknown_function_00322F5E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00322EB0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00322EB5  56                              push rsi
00322EB6  48 83 EC 20                     sub rsp, 0x20
00322EBA  49 8B D8                        mov rbx, r8
00322EBD  48 8B F2                        mov rsi, rdx
00322EC0  85 C9                           test ecx, ecx
00322EC2  0F 85 96 00 00 00               jne 0x140322f5e
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiGetPteMappingSet(int a1, __int64 a2, __int64 a3)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void MiGetPteMappingSet(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00322EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00322EB0[BB_00322EB0]
```
