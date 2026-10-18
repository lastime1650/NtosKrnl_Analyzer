# sub_006D8F9A

- RVA: `0x006D8F9A`–`0x006D8FB2` (길이 `24` bytes)
- VA: `0x00000001406D8F9A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065068`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006D8F9D` → [FsRtlRemovePerStreamContext + 0x9B](../26/FsRtlRemovePerStreamContext_function_00267760.md) (`tail-transfer`)
  - `0x006D8FA7` → [FsRtlRemovePerStreamContext + 0x73](../26/FsRtlRemovePerStreamContext_function_00267760.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006D8F9A  48 3B C1                        cmp rax, rcx
006D8F9D  0F 84 58 E8 B8 FF               je 0x1402677fb
006D8FA3  48 39 70 10                     cmp qword ptr [rax + 0x10], rsi
006D8FA7  0F 84 26 E8 B8 FF               je 0x1402677d3
006D8FAD  48 8B 00                        mov rax, qword ptr [rax]
006D8FB0  EB E8                           jmp 0x1406d8f9a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006D8F9A(__int64 a1)
{
    goto loc_006D8F9A;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006D8F9A(int64_t Arg1)
{
    goto loc_006D8F9A;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D8F9A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D8F9A[BB_006D8F9A]
  bb_006D8FA3[BB_006D8FA3]
  bb_006D8FAD[BB_006D8FAD]
  bb_006D8F9A -->|fallthrough| bb_006D8FA3
  bb_006D8FA3 -->|fallthrough| bb_006D8FAD
  bb_006D8FAD -->|branch| bb_006D8F9A
```
