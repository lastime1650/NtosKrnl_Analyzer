# SepRmProcessCreationCommandLineAuditSettingsWrkr

- RVA: `0x00609F60`–`0x00609F90` (길이 `48` bytes)
- VA: `0x0000000140609F60`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00609F6D` → [PsIsCurrentThreadInServerSilo](../43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00609F79` → RVA `0x00F04AC4` (`.data`; write)
- `0x00609F7F` → RVA `0x00F04AC8` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00609F60  40 53                           push rbx
00609F62  48 83 EC 20                     sub rsp, 0x20
00609F66  83 62 28 00                     and dword ptr [rdx + 0x28], 0
00609F6A  48 8B D9                        mov rbx, rcx
00609F6D  E8 6E C3 E2 FF                  call 0x1404362e0
00609F72  84 C0                           test al, al
00609F74  75 13                           jne 0x140609f89
00609F76  8A 43 2C                        mov al, byte ptr [rbx + 0x2c]
00609F79  88 05 45 AB 8F 00               mov byte ptr [rip + 0x8fab45], al
00609F7F  C7 05 3F AB 8F 00 01 00 00 00   mov dword ptr [rip + 0x8fab3f], 1
00609F89  48 83 C4 20                     add rsp, 0x20
00609F8D  5B                              pop rbx
00609F8E  C3                              ret
00609F8F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepRmProcessCreationCommandLineAuditSettingsWrkr(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        result = *(unsigned __int8 *)(a1 + 44);
        *(unsigned __int8 *)(v_rip + 9415493) = (unsigned __int8)(result);
        *(unsigned int *)(v_rip + 9415487) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepRmProcessCreationCommandLineAuditSettingsWrkr(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PsIsCurrentThreadInServerSilo(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        result = *(uint8_t *)(arg1 + 0x2C);
        *(uint8_t *)(v_rip + 0x8FAB45) = (uint8_t)(result);
        *(uint32_t *)(v_rip + 0x8FAB3F) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2C` | `8` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00609F60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00609F60[BB_00609F60]
  bb_00609F76[BB_00609F76]
  bb_00609F89[BB_00609F89]
  bb_00609F8F[BB_00609F8F]
  bb_00609F60 -->|branch| bb_00609F89
  bb_00609F60 -->|fallthrough| bb_00609F76
  bb_00609F76 -->|flow| bb_00609F89
```
