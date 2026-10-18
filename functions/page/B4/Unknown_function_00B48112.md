# sub_00B48112

- RVA: `0x00B48112`–`0x00B48128` (길이 `22` bytes)
- VA: `0x0000000140B48112`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA210`
- 디코드: `5`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B4811C` → RVA `0x00E2D870` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B48123` → [MiLogRetpolineImageLoadEvents + 0x33](../A9/MiLogRetpolineImageLoadEvents_function_00A996F0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B48112  48 89 10                        mov qword ptr [rax], rdx
00B48115  48 89 48 08                     mov qword ptr [rax + 8], rcx
00B48119  48 89 01                        mov qword ptr [rcx], rax
00B4811C  48 89 05 4D 57 2E 00            mov qword ptr [rip + 0x2e574d], rax
00B48123  E9 FB 15 F5 FF                  jmp 0x140a99723
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B48112(__int64 a1, __int64 a2)
{
    *(unsigned __int64 *)(result) = a2;
    *(unsigned __int64 *)(result + 8) = a1;
    *(unsigned __int64 *)(a1) = result;
    *(unsigned __int64 *)(v_rip + 3037005) = result;
}
```

## 5. (Beta) C Style

```c
void sub_00B48112(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(result) = Arg2;
    *(void **)(result + 0x8) = Arg1;
    *(uint64_t *)(arg1) = result;
    *(uint64_t *)(v_rip + 0x2E574D) = result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B48112&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B48112[BB_00B48112]
```
