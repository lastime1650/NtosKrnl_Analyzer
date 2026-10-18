# WmipAcquireSmbiosLockShared

- RVA: `0x00A4F224`–`0x00A4F24D` (길이 `41` bytes)
- VA: `0x0000000140A4F224`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A4F242` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)

### Direct callers
- [WmipFindSMBiosStructure](../7B/WmipFindSMBiosStructure_function_007B2944.md) at `0x007B296B`
- [WmipGetSMBiosTableData](WmipGetSMBiosTableData_function_00A4F078.md) at `0x00A4F099`

### Static image references
- `0x00A4F231` → RVA `0x00EFFB40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4F242` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4F224  48 83 EC 28                     sub rsp, 0x28
00A4F228  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A4F231  48 8D 0D 08 09 4B 00            lea rcx, [rip + 0x4b0908]
00A4F238  B2 01                           mov dl, 1
00A4F23A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A4F241  90                              nop
00A4F242  E8 79 29 7C FF                  call 0x140211bc0
00A4F247  48 83 C4 28                     add rsp, 0x28
00A4F24B  C3                              ret
00A4F24C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WmipAcquireSmbiosLockShared(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireResourceSharedLite(v_rip + 4917512, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void WmipAcquireSmbiosLockShared(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireResourceSharedLite(v_rip + 4917512, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4F224&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4F224[BB_00A4F224]
  bb_00A4F24C[BB_00A4F24C]
```
