# KcsaniInsertInDatabase

- RVA: `0x005AF880`–`0x005AF8A0` (길이 `32` bytes)
- VA: `0x00000001405AF880`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C978C`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KcsanValidateAddress](KcsanValidateAddress_function_005AF5E0.md) at `0x005AF746`

### Static image references
- `0x005AF886` → RVA `0x00F59CE0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x005AF89A` → [sub_005AF973](Unknown_function_005AF973.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
005AF880  40 57                           push rdi
005AF882  48 83 EC 20                     sub rsp, 0x20
005AF886  44 8B 0D 53 A4 9A 00            mov r9d, dword ptr [rip + 0x9aa453]
005AF88D  4C 8B DA                        mov r11, rdx
005AF890  48 8B F9                        mov rdi, rcx
005AF893  41 81 F9 00 01 00 00            cmp r9d, 0x100
005AF89A  0F 87 D3 00 00 00               ja 0x1405af973
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KcsaniInsertInDatabase(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void KcsaniInsertInDatabase(int64_t Arg1, int64_t Arg2)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005AF880&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005AF880[BB_005AF880]
```
