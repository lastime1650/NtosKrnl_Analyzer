# MiCoalescePageFileBitmapsCache

- RVA: `0x003E4540`–`0x003E455D` (길이 `29` bytes)
- VA: `0x00000001403E4540`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094D80`
- 디코드: `8`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) at `0x0028427F`
- [MiFinishPageFileExtension](../4D/MiFinishPageFileExtension_function_004D5EB4.md) at `0x004D5F4C`
- [sub_006F503A](../6F/Unknown_function_006F503A.md) at `0x006F521E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003E4557` → [sub_003E47A6](Unknown_function_003E47A6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E4540  48 8B C4                        mov rax, rsp
003E4543  57                              push rdi
003E4544  41 55                           push r13
003E4546  48 83 EC 68                     sub rsp, 0x68
003E454A  F6 81 AF 00 00 00 01            test byte ptr [rcx + 0xaf], 1
003E4551  41 8B F8                        mov edi, r8d
003E4554  4C 8B E9                        mov r13, rcx
003E4557  0F 85 49 02 00 00               jne 0x1403e47a6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCoalescePageFileBitmapsCache(__int64 a1, __int64 a2, int a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (104);
}
```

## 5. (Beta) C Style

```c
int64_t MiCoalescePageFileBitmapsCache(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (104);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xAF` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E4540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E4540[BB_003E4540]
```
