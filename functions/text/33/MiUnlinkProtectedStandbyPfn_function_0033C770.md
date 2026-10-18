# MiUnlinkProtectedStandbyPfn

- RVA: `0x0033C770`–`0x0033C792` (길이 `34` bytes)
- VA: `0x000000014033C770`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076FF4`
- 디코드: `7`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00287A62](../28/Unknown_function_00287A62.md) at `0x00287C64`
- [sub_0033DA89](Unknown_function_0033DA89.md) at `0x0033DA8C`

### Static image references
- `0x0033C788` → RVA `0x00E35C00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0033C770  48 83 EC 28                     sub rsp, 0x28
0033C774  4C 8B 01                        mov r8, qword ptr [rcx]
0033C777  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
0033C781  4C 8B 49 18                     mov r9, qword ptr [rcx + 0x18]
0033C785  49 8B D0                        mov rdx, r8
0033C788  48 8B 0D 71 94 AF 00            mov rcx, qword ptr [rip + 0xaf9471]
0033C78F  4D 8B D1                        mov r10, r9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUnlinkProtectedStandbyPfn(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUnlinkProtectedStandbyPfn(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0033C770&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0033C770[BB_0033C770]
```
