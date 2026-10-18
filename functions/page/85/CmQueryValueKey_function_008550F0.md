# CmQueryValueKey

- RVA: `0x008550F0`–`0x00855118` (길이 `40` bytes)
- VA: `0x00000001408550F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A044`
- 디코드: `10`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmQueryValueKeyCallout](../A1/CmQueryValueKeyCallout_function_00A19D70.md) at `0x00A19DA4`

### Static image references
- `0x00855100` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008550F0  4C 8B DC                        mov r11, rsp
008550F3  55                              push rbp
008550F4  57                              push rdi
008550F5  49 8D 6B A8                     lea rbp, [r11 - 0x58]
008550F9  48 81 EC 48 01 00 00            sub rsp, 0x148
00855100  48 8B 05 39 56 5B 00            mov rax, qword ptr [rip + 0x5b5639]
00855107  48 33 C4                        xor rax, rsp
0085510A  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0085510E  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
00855115  0F 57 C0                        xorps xmm0, xmm0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmQueryValueKey(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (328);
    result = (*(unsigned __int64 *)(v_rip + 5985849)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 88 + 16) = result;
    return *(unsigned __int64 *)(v_rsp - 88 + 136);
}
```

## 5. (Beta) C Style

```c
void CmQueryValueKey(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (328);
    result = (*(uint64_t *)(v_rip + 0x5B5639)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x58 + 0x10) = result;
    return *(uint64_t *)(local_rsp - 0x58 + 0x88);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008550F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008550F0[BB_008550F0]
```
