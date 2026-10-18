# SSHSupportEtwEventEnabled

- RVA: `0x00391484`–`0x0039149A` (길이 `22` bytes)
- VA: `0x0000000140391484`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0039148F` → [EtwEventEnabled](EtwEventEnabled_function_00392450.md) (function, `0x00392450`)

### Direct callers
- [SshpFlushBlockerDataCache](../../page/A6/SshpFlushBlockerDataCache_function_00A606F4.md) at `0x00A6073E`
- [SshpTracingRundownCollectionState](../../page/A8/SshpTracingRundownCollectionState_function_00A8E534.md) at `0x00A8E577`
- [SshpTracingWriteCollectionStateChange](../../page/AA/SshpTracingWriteCollectionStateChange_function_00AADE8C.md) at `0x00AADEC5`

### Static image references
- `0x00391488` → RVA `0x00F07010` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00391484  48 83 EC 28                     sub rsp, 0x28
00391488  48 8B 0D 81 5B B7 00            mov rcx, qword ptr [rip + 0xb75b81]
0039148F  E8 BC 0F 00 00                  call 0x140392450
00391494  48 83 C4 28                     add rsp, 0x28
00391498  C3                              ret
00391499  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SSHSupportEtwEventEnabled(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 12016513), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SSHSupportEtwEventEnabled(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xB75B81), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00391484&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00391484[BB_00391484]
  bb_00391499[BB_00391499]
```
