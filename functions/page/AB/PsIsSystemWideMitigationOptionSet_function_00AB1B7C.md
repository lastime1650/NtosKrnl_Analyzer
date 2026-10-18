# PsIsSystemWideMitigationOptionSet

- RVA: `0x00AB1B7C`–`0x00AB1B9C` (길이 `32` bytes)
- VA: `0x0000000140AB1B7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7CE7`

### Static image references
- `0x00AB1B80` → RVA `0x00FC7108` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB1B7C  48 83 EC 28                     sub rsp, 0x28
00AB1B80  48 8B 0D 81 55 51 00            mov rcx, qword ptr [rip + 0x515581]
00AB1B87  33 C0                           xor eax, eax
00AB1B89  48 C1 E9 24                     shr rcx, 0x24
00AB1B8D  80 E1 0F                        and cl, 0xf
00AB1B90  80 F9 06                        cmp cl, 6
00AB1B93  0F 94 C0                        sete al
00AB1B96  48 83 C4 28                     add rsp, 0x28
00AB1B9A  C3                              ret
00AB1B9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsIsSystemWideMitigationOptionSet(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    a1 = (*(unsigned __int64 *)(v_rip + 5330305)) >> (36);
    a1 = (unsigned __int8)((a1) & (15));
    result = (((unsigned __int8)(a1)) == 6) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PsIsSystemWideMitigationOptionSet(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    a1 = (*(uint64_t *)(v_rip + 0x515581)) >> (36);
    a1 = (uint8_t)((a1) & (15));
    result = (((uint8_t)(a1)) == 6) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB1B7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB1B7C[BB_00AB1B7C]
  bb_00AB1B9B[BB_00AB1B9B]
```
