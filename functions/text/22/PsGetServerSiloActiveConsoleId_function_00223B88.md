# PsGetServerSiloActiveConsoleId

- RVA: `0x00223B88`–`0x00223BA1` (길이 `25` bytes)
- VA: `0x0000000140223B88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00223B8C` → [PsGetServerSiloGlobals](PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)

### Direct callers
- [IopGetThreadActiveConsoleId](../../page/AB/IopGetThreadActiveConsoleId_function_00AB4EE8.md) at `0x00AB4EF4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00223B88  48 83 EC 28                     sub rsp, 0x28
00223B8C  E8 0F 15 00 00                  call 0x1402250a0
00223B91  48 8B 80 08 05 00 00            mov rax, qword ptr [rax + 0x508]
00223B98  8B 40 04                        mov eax, dword ptr [rax + 4]
00223B9B  48 83 C4 28                     add rsp, 0x28
00223B9F  C3                              ret
00223BA0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetServerSiloActiveConsoleId(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsGetServerSiloGlobals(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 1288) + 4));
}
```

## 5. (Beta) C Style

```c
void PsGetServerSiloActiveConsoleId(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsGetServerSiloGlobals(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x508) + 0x4));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00223B88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00223B88[BB_00223B88]
  bb_00223BA0[BB_00223BA0]
```
